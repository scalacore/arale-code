"""STDIO integration test for arale-code server."""

import json

import anyio
import pytest
import yaml
from fastmcp.client import Client
from fastmcp.client.transports import StdioTransport


@pytest.mark.asyncio
async def test_server_stdio_subprocess() -> None:
    transport = StdioTransport(
        command="uv",
        args=["run", "arale-code"],
    )

    with anyio.fail_after(20):
        async with Client(transport=transport) as client:
            tools = await client.list_tools()
            tool_names = [t.name for t in tools]
            assert "list_procedures" in tool_names
            assert "list_instructions" in tool_names

            res = await client.call_tool("list_procedures", {})
            assert not res.is_error
            data = json.loads(res.data)
            assert data["schema_version"] == 1
            assert len(data["documents"]) == 21

            guide = await client.read_resource("arale://procedure/guide")
            assert guide[0].mime_type == "application/yaml"
            content = yaml.safe_load(guide[0].text)
            assert content["meta"]["version"] == "1.7"
            assert content["protocol"]["ledger"]["display_policy"]["default_view"] == "concise"
