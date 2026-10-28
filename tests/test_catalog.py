"""Unit tests for InstructionCatalog and ProcedureCatalog."""

import json

import pytest

from arale_code.catalog import InstructionCatalog, UnknownInstructionError
from arale_code.procedures import ProcedureCatalog, UnknownProcedureDocumentError


def test_procedure_catalog_contents() -> None:
    catalog = ProcedureCatalog()
    summaries = catalog.list_documents()

    # Confirm 21 entries
    assert len(summaries) == 21

    # Check order: guide first, then p01 through p20
    assert summaries[0].id == "guide"
    assert summaries[0].code == "GUIDE"
    assert summaries[0].kind == "guide"
    assert summaries[0].uri == "arale://procedure/guide"

    for i in range(1, 21):
        num_str = f"{i:02d}"
        expected_code = f"P{num_str}"
        assert summaries[i].code == expected_code
        assert summaries[i].id.startswith(f"p{num_str}")
        assert summaries[i].kind == "procedure"
        assert summaries[i].uri == f"arale://procedure/{summaries[i].id}"


def test_procedure_catalog_aliases_and_get() -> None:
    catalog = ProcedureCatalog()

    # Get guide by canonical ID and alias
    guide_content = catalog.get_document("guide")
    assert "Control Guide" in guide_content
    assert catalog.get_document("00-guide") == guide_content
    assert catalog.get_document("00") == guide_content

    # Get p01 by canonical ID and alias
    p01_content = catalog.get_document("p01-project-reconnaissance")
    assert "Project Reconnaissance" in p01_content
    assert catalog.get_document("p01") == p01_content
    assert catalog.get_document("01") == p01_content


def test_procedure_catalog_unknown_id_error() -> None:
    catalog = ProcedureCatalog()
    with pytest.raises(UnknownProcedureDocumentError) as exc_info:
        catalog.get_document("unknown-id")
    assert "Unknown procedure id: unknown-id" in str(exc_info.value)


def test_procedure_catalog_json_manifest() -> None:
    catalog = ProcedureCatalog()
    manifest_str = catalog.to_json_manifest()
    data = json.loads(manifest_str)
    assert data["schema_version"] == 1
    assert len(data["documents"]) == 21
    assert data["documents"][0]["id"] == "guide"


def test_instruction_catalog_contents() -> None:
    catalog = InstructionCatalog()
    summaries = catalog.list_documents()

    assert len(summaries) == 4
    # Check descending priority order: 100, 90, 80, 70
    assert [s.id for s in summaries] == [
        "design-spec",
        "implementation-plan",
        "code-quality",
        "testing",
    ]
    assert [s.priority for s in summaries] == [100, 90, 80, 70]


def test_instruction_catalog_get_and_unknown() -> None:
    catalog = InstructionCatalog()
    content = catalog.get_document("design-spec")
    assert "# Design Specification" in content

    with pytest.raises(UnknownInstructionError) as exc_info:
        catalog.get_document("invalid-id")
    assert "Unknown instruction id: invalid-id" in str(exc_info.value)
