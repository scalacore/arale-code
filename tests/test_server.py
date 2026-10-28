"""In-memory client tests verifying the FastMCP server contract."""

import json

import pytest
from fastmcp.client import Client

from arale_code.server import SERVER_INSTRUCTIONS, instruction_catalog, main, mcp, procedure_catalog


def test_server_instructions_offer_guide_entry_without_enforcing_read_order() -> None:
    assert "read arale://procedure/guide first" in SERVER_INSTRUCTIONS
    assert "read the selected arale://procedure/{id} in full" in SERVER_INSTRUCTIONS


def test_main_starts_stdio_without_update_banner(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[dict[str, object]] = []
    monkeypatch.setattr(mcp, "run", lambda **kwargs: calls.append(kwargs))

    main()

    assert calls == [{"transport": "stdio", "show_banner": False}]


@pytest.mark.asyncio
async def test_server_tools_list_and_call() -> None:
    async with Client(mcp) as client:
        tools = await client.list_tools()
        tool_names = [t.name for t in tools]
        assert "list_instructions" in tool_names
        assert "list_procedures" in tool_names
        assert len(tool_names) == 2

        # Call list_instructions
        res_inst = await client.call_tool("list_instructions", {})
        assert not res_inst.is_error
        data_inst = json.loads(res_inst.data)
        assert data_inst["schema_version"] == 1
        assert len(data_inst["documents"]) == 4

        # Call list_procedures
        res_proc = await client.call_tool("list_procedures", {})
        assert not res_proc.is_error
        data_proc = json.loads(res_proc.data)
        assert data_proc["schema_version"] == 1
        assert len(data_proc["documents"]) == 21


@pytest.mark.asyncio
async def test_server_resources_catalogs() -> None:
    async with Client(mcp) as client:
        resources = await client.list_resources()
        uris = [r.uri for r in resources]
        assert "instructions://catalog" in uris
        assert "arale://catalog" in uris

        # Read instructions://catalog
        contents_inst = await client.read_resource("instructions://catalog")
        assert len(contents_inst) == 1
        assert contents_inst[0].mime_type == "application/json"
        data_inst = json.loads(contents_inst[0].text)
        assert data_inst["schema_version"] == 1
        assert len(data_inst["documents"]) == 4

        # Read arale://catalog
        contents_proc = await client.read_resource("arale://catalog")
        assert len(contents_proc) == 1
        assert contents_proc[0].mime_type == "application/json"
        data_proc = json.loads(contents_proc[0].text)
        assert data_proc["schema_version"] == 1
        assert len(data_proc["documents"]) == 21


@pytest.mark.asyncio
async def test_server_read_all_procedure_resources_and_mimes() -> None:
    async with Client(mcp) as client:
        for proc in procedure_catalog.list_documents():
            expected_text = procedure_catalog.get_document(proc.id)
            contents = await client.read_resource(proc.uri)
            assert len(contents) == 1
            assert contents[0].mime_type == "application/yaml"
            assert contents[0].text == expected_text


@pytest.mark.asyncio
async def test_server_read_all_instruction_resources_and_mimes() -> None:
    async with Client(mcp) as client:
        for inst in instruction_catalog.list_documents():
            expected_text = instruction_catalog.get_document(inst.id)
            contents = await client.read_resource(inst.uri)
            assert len(contents) == 1
            assert contents[0].mime_type == "text/markdown"
            assert contents[0].text == expected_text


@pytest.mark.asyncio
async def test_server_unknown_resource_errors() -> None:
    async with Client(mcp) as client:
        with pytest.raises(Exception) as exc_inst:
            await client.read_resource("instructions://document/unknown-id")
        assert "Unknown instruction id: unknown-id" in str(exc_inst.value)

        with pytest.raises(Exception) as exc_proc:
            await client.read_resource("arale://procedure/unknown-id")
        assert "Unknown procedure id: unknown-id" in str(exc_proc.value)


@pytest.mark.asyncio
async def test_server_prompt_rendering() -> None:
    async with Client(mcp) as client:
        for inst_id in instruction_catalog.list_ids():
            prompt_res = await client.get_prompt(
                "apply_instruction", {"id": inst_id, "task": "Validate implementation"}
            )
            assert len(prompt_res.messages) == 1
            msg = prompt_res.messages[0]
            assert msg.role == "user"
            assert f"Instruction ID: {inst_id}" in msg.content.text
            assert "Task:\nValidate implementation" in msg.content.text
            assert "Execution rules:" in msg.content.text


@pytest.mark.asyncio
async def test_server_prompt_validation_errors() -> None:
    async with Client(mcp) as client:
        # Empty task
        with pytest.raises(Exception) as exc_empty:
            await client.get_prompt("apply_instruction", {"id": "testing", "task": "   "})
        assert "Task must not be empty or whitespace-only" in str(exc_empty.value)

        # Oversized task
        with pytest.raises(Exception) as exc_large:
            await client.get_prompt("apply_instruction", {"id": "testing", "task": "x" * 4001})
        assert "Task must not exceed 4000 characters" in str(exc_large.value)

        # Unknown id
        with pytest.raises(Exception) as exc_unknown:
            await client.get_prompt("apply_instruction", {"id": "unknown-id", "task": "Valid task"})
        assert "Unknown instruction id: unknown-id" in str(exc_unknown.value)
