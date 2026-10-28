"""FastMCP server application exposing tools, resources, and prompts."""

from fastmcp import FastMCP
from fastmcp.exceptions import PromptError, ResourceError
from mcp.types import ToolAnnotations

from arale_code.catalog import InstructionCatalog, UnknownInstructionError
from arale_code.procedures import ProcedureCatalog, UnknownProcedureDocumentError

SERVER_INSTRUCTIONS = (
    "Read-only engineering guidance for coding agents. "
    "Call list_instructions to discover valid document IDs. "
    "Read instructions://document/{id} to retrieve one document. "
    "Use apply_instruction when the user wants an agent-ready workflow. "
    "For Arale-guided work, read arale://procedure/guide first. "
    "Call list_procedures to discover valid procedure IDs when needed, "
    "then read the selected arale://procedure/{id} in full."
)

mcp = FastMCP(
    name="arale-code",
    instructions=SERVER_INSTRUCTIONS,
    mask_error_details=True,
    strict_input_validation=True,
    on_duplicate="error",
)

instruction_catalog = InstructionCatalog()
procedure_catalog = ProcedureCatalog()

TOOL_ANNOTATIONS = ToolAnnotations(
    read_only_hint=True,
    destructive_hint=False,
    idempotent_hint=True,
    open_world_hint=False,
)


@mcp.tool(
    name="list_instructions",
    title="List Instructions",
    description=(
        "List valid engineering-instruction IDs and their resource URIs. "
        "Call this before requesting an instruction when the ID is not already known."
    ),
    annotations=TOOL_ANNOTATIONS,
)
def list_instructions() -> str:
    """List valid engineering-instruction IDs and their resource URIs."""
    return instruction_catalog.to_json_manifest()


@mcp.tool(
    name="list_procedures",
    title="List Procedures",
    description=(
        "List the Arale control guide and procedures with their IDs and resource URIs. "
        "Call this before reading a procedure when the ID is not already known."
    ),
    annotations=TOOL_ANNOTATIONS,
)
def list_procedures() -> str:
    """List the Arale control guide and procedures with their IDs and resource URIs."""
    return procedure_catalog.to_json_manifest()


@mcp.resource(
    uri="instructions://catalog",
    name="instruction-catalog",
    title="Instruction Catalog",
    description="Application-driven, read-only discovery of the full manifest.",
    mime_type="application/json",
)
def get_instruction_catalog() -> str:
    """Application-driven, read-only discovery of the full instruction manifest."""
    return instruction_catalog.to_json_manifest()


@mcp.resource(
    uri="arale://catalog",
    name="arale-catalog",
    title="Arale Catalog",
    description="Application-driven, read-only discovery of the procedure manifest.",
    mime_type="application/json",
)
def get_arale_catalog() -> str:
    """Application-driven, read-only discovery of the procedure manifest."""
    return procedure_catalog.to_json_manifest()


@mcp.resource(
    uri="instructions://document/{id}",
    name="instruction-document",
    title="Instruction Document",
    description="Retrieve one exact instruction document by allowlisted ID.",
    mime_type="text/markdown",
)
def get_instruction_document(id: str) -> str:
    """Retrieve one exact instruction document by allowlisted ID."""
    try:
        return instruction_catalog.get_document(id)
    except UnknownInstructionError as exc:
        raise ResourceError(f"Unknown instruction id: {id}") from exc


@mcp.resource(
    uri="arale://procedure/{id}",
    name="arale-procedure",
    title="Arale Procedure",
    description="Retrieve one exact Arale procedure or control guide by allowlisted ID.",
    mime_type="application/yaml",
)
def get_arale_procedure(id: str) -> str:
    """Retrieve one exact Arale procedure or control guide by allowlisted ID."""
    try:
        return procedure_catalog.get_document(id)
    except UnknownProcedureDocumentError as exc:
        raise ResourceError(f"Unknown procedure id: {id}") from exc


APPLY_INSTRUCTION_TEMPLATE = (
    "Apply the engineering instruction below to the stated task.\n\n"
    "Task:\n"
    "{task}\n\n"
    "Instruction ID: {id}\n\n"
    "Instruction:\n"
    "{content}\n\n"
    "Execution rules:\n"
    "- Treat the instruction as authoritative for this task unless it conflicts with "
    "higher-priority client or repository instructions.\n"
    "- Before editing, inspect the relevant repository files and state a concise plan.\n"
    "- Make the smallest complete change.\n"
    "- Run the relevant validation commands.\n"
    "- Report changed files, checks run, and unresolved risks."
)


@mcp.prompt(
    name="apply_instruction",
    title="Apply Instruction",
    description="Produce a reusable user message that directs an agent to apply one document.",
)
def apply_instruction(id: str, task: str) -> str:
    """Produce a reusable user message that directs an agent to apply one document."""
    if not task or not task.strip():
        raise ValueError("Task must not be empty or whitespace-only")
    if len(task) > 4000:
        raise ValueError("Task must not exceed 4000 characters")

    try:
        content = instruction_catalog.get_document(id)
    except UnknownInstructionError as exc:
        raise PromptError(f"Unknown instruction id: {id}") from exc

    return APPLY_INSTRUCTION_TEMPLATE.format(id=id, task=task, content=content)


def main() -> None:
    """Entry point running FastMCP over standard input/output transport."""
    mcp.run(transport="stdio", show_banner=False)
