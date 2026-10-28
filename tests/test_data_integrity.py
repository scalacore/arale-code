"""Data integrity tests for arale-code YAML procedures and Markdown instructions."""

import hashlib
import re
from pathlib import Path
from typing import Any

import pytest
import yaml

from arale_code.procedures import PROCEDURE_DEFINITIONS

REPO_ROOT = Path(__file__).resolve().parent.parent

PROCEDURES_DIR = REPO_ROOT / "src" / "arale_code" / "procedures"
INSTRUCTIONS_DIR = REPO_ROOT / "src" / "arale_code" / "instructions"

MAX_FILE_SIZE_BYTES = 65536

PROCEDURE_EXPECTED_HASHES: dict[str, tuple[int, str]] = {
    "00-guide.yaml": (
        21065,
        "c015d5b409fdd06b8ae4b05e07d012cce99150cc9b780b60fa4591e09afe344a",
    ),
    "01-project-reconnaissance.yaml": (
        13745,
        "39578c467c53ca1fb3d5def8783d5ee658e99491973ded4796f21ee92bd23dbe",
    ),
    "02-initial-state-baseline.yaml": (
        15142,
        "4ad903e82857f31a821e19ab7ab63a1a60122c777e4b8024a0bc54da0585119e",
    ),
    "03-environment-diagnosis.yaml": (
        14034,
        "c219ff055e1b2dd357273f208e05dce819fd844a5915e346c55ed9d3d98e5993",
    ),
    "04-mandate-clarification.yaml": (
        12555,
        "02721613e5ab5ca27314d8193c47d88473af2cefc87865be42c5548bd4e71fa2",
    ),
    "05-behavior-specification.yaml": (
        12766,
        "6c2be0baa50fa364e4386f4bbd0cce7f195afedd9991235201329aa722824a23",
    ),
    "06-interaction-design.yaml": (
        13777,
        "34517667d196843f10ff5fd3533de391551d1434d9e170d7fa47b0c2612edfbd",
    ),
    "07-technical-design.yaml": (
        14049,
        "eb6c9c21734cb5eec6ae6e615e009965256719fd7817293c85b1466c582402cb",
    ),
    "08-contracts-compatibility.yaml": (
        16566,
        "0f332cdc28e13d41dace4625916fe1ad6e95cacba46ce445c61f6d6f410465f1",
    ),
    "09-plan-tasks-dependencies.yaml": (
        14650,
        "451ef6639fb3b801c70a993acc61af1a1317490cddceeed0a667624d1c194847",
    ),
    "10-coherence-coverage.yaml": (
        14364,
        "7393c5abc044c5dfd6e9f8eddf0d7b870b5ca9977e326826b0517a5e247fada5",
    ),
    "11-malfunction-diagnosis.yaml": (
        15603,
        "0bc02f6814cb973fd2311284042ae9e8b24eb091823fe93e61ed6d2f94d52f14",
    ),
    "12-task-execution.yaml": (
        16629,
        "6d962b4966689a1564cd064bbed5d21e3e38bd36cd63f41754903015c731a924",
    ),
    "13-controlled-refactoring.yaml": (
        14188,
        "27ca3a90483c5dfbd789a4d65a29637d46f32d35e3dc7ec32083c35d37aeb5dd",
    ),
    "14-performance-optimization.yaml": (
        14512,
        "7c4efd6e5f8050993cd8fdb5316656bae4501cbaaf1afde59de0e52a99cd6913",
    ),
    "15-testing-verification.yaml": (
        15329,
        "fbd12038b9c713d55b0f34c1a18018c8ce579564e1aae1c1d8f500268ed6e63c",
    ),
    "16-change-review.yaml": (
        13513,
        "a3920e47dc29a90339010419cda63050a0507ded3ac253277a701477a2f06b12",
    ),
    "17-security-data-integrity.yaml": (
        13932,
        "a7bb9402f0011dddb24b6b9cb984cf4c7c9d86bfc365a4351f087a7bb5ed67cb",
    ),
    "18-integration-migrations.yaml": (
        15489,
        "ebf7a86c5767cbefa02aa86dce9505846acc29fafe771aa0abe00f85f9279625",
    ),
    "19-state-recovery-replanning.yaml": (
        15796,
        "771486f74d2c6252a01b8d53a04e073dee1b6d659cfa153fd4181f1d1194cf91",
    ),
    "20-acceptance-delivery.yaml": (
        15147,
        "deb9abc4a0de1cb47cc8fd59345289279dc82f9b9a4081fdfe7cc77ef4d06d87",
    ),
}

INSTRUCTION_EXPECTED_HASHES: dict[str, tuple[int, str]] = {
    "code-quality.md": (
        973,
        "ac2de6053253c7f056fa603a363b348c051fd7a8c015d7268e6b9b0f3abc842c",
    ),
    "design-spec.md": (
        1208,
        "bc148c542e17290cdd26329ee93f5f461cc4b6d0863122faf5620b4382ebef3b",
    ),
    "implementation-plan.md": (
        772,
        "be9bc5bb969eb50ce4e5da37a3a4bd2675cca793e4e66eef49218c116c417245",
    ),
    "testing.md": (
        894,
        "1113eb2ad6142750c508f1cf4d3d7eee73eed6e6c425a652e83ffd26d1edc927",
    ),
}


def _unique_mapping(loader: Any, node: Any) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str):
            raise ValueError("Procedure YAML keys must be strings")
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


def _load_procedure_yaml(text: str) -> dict[str, Any]:
    """Parse an asset for offline structural checks, without runtime changes."""
    loader = yaml.SafeLoader(text)
    loader.yaml_constructors = {
        **loader.yaml_constructors,
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG: _unique_mapping,
    }
    try:
        data = loader.get_single_data()
    finally:
        loader.dispose()
    if not isinstance(data, dict):
        raise ValueError("Procedure YAML must contain a mapping")
    return data


def _decode_asset(raw: bytes) -> str:
    """Decode bundled text for explicit encoding and newline checks."""
    if raw.startswith(b"\xef\xbb\xbf") or b"\r" in raw:
        raise ValueError("Bundled text must use UTF-8 without BOM and LF endings")
    return raw.decode("utf-8")


def _validate_procedure_asset(raw: bytes, file_name: str) -> dict[str, Any]:
    """Validate the editorial asset contract in tests, not in the server."""
    if len(raw) > MAX_FILE_SIZE_BYTES:
        raise ValueError("Procedure asset exceeds byte limit")
    data = _load_procedure_yaml(_decode_asset(raw))
    entry = next(item for item in PROCEDURE_DEFINITIONS if item["filename"] == file_name)
    is_guide = entry["kind"] == "guide"
    meta = data.get("meta") if is_guide else data
    if not isinstance(meta, dict):
        raise ValueError("Missing guide metadata")
    expected = {
        "id": entry["code"],
        "title": entry["title"],
        "file": file_name,
        "language": "en",
        "kind": "control_guide" if is_guide else "autonomous_prompt",
    }
    if any(meta.get(key) != value for key, value in expected.items()):
        raise ValueError("Procedure metadata differs from the public catalog")
    if meta.get("version") not in {"1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7"}:
        raise ValueError("Unsupported content version")
    sections = (
        ("boot", "router", "protocol")
        if is_guide
        else (
            "purpose",
            "when_to_use",
            "context_and_prerequisites",
            "mandate_and_approval",
            "limits_and_stop_conditions",
            "verification_and_completion",
            "report_and_closure",
        )
    )
    if any(not isinstance(data.get(key), dict) or not data[key] for key in sections):
        raise ValueError("Missing procedure or guide section")
    if is_guide:
        return data
    modes = data["mandate_and_approval"].get("modes")
    if not isinstance(modes, dict) or not modes:
        raise ValueError("Missing procedure modes")
    if any(not isinstance(value, str) or not value.strip() for value in modes.values()):
        raise ValueError("Mode descriptions must be nonempty text")
    steps = data.get("procedure")
    if not isinstance(steps, list) or not steps:
        raise ValueError("Missing procedure steps")
    numbers: set[int] = set()
    for step in steps:
        if not isinstance(step, dict):
            raise ValueError("Procedure steps must be mappings")
        number, action = step.get("step"), step.get("action")
        if type(number) is not int or number < 1 or number in numbers:
            raise ValueError("Procedure step numbers must be unique positive integers")
        if not isinstance(action, str) or not action.strip():
            raise ValueError("Procedure actions must be nonempty text")
        numbers.add(number)
    return data


def test_p05_preserves_source_actor_scope_for_repeated_requests() -> None:
    """Repeated/stateful requirements must not acquire an invented same-actor rule."""
    data = _load_procedure_yaml(
        (PROCEDURES_DIR / "05-behavior-specification.yaml").read_text(encoding="utf-8")
    )
    step = next(item for item in data["procedure"] if item["step"] == 5)
    action = step["action"].casefold()

    assert "source states an actor scope" in action
    assert "do not narrow it to the actor" in action
    assert "previous action" in action
    assert "open decision" in action


def test_p10_checks_combined_predicate_coverage() -> None:
    """Coverage review must distinguish a specified AND/OR rule from its alternative."""
    data = _load_procedure_yaml(
        (PROCEDURES_DIR / "10-coherence-coverage.yaml").read_text(encoding="utf-8")
    )
    step = next(item for item in data["procedure"] if item["step"] == 6)
    action = step["action"].casefold()

    assert "combined input" in action
    assert "distinguish" in action
    assert "conjunction" in action
    assert "disjunction" in action
    assert "unresolved" in action
    assert "do not assume" in action


def test_guide_route_and_record_structure() -> None:
    """Keep the routing and visible record contract through Guide revisions."""
    raw = (PROCEDURES_DIR / "00-guide.yaml").read_bytes()
    guide = _load_procedure_yaml(_decode_asset(raw))
    router = guide["router"]
    protocol = guide["protocol"]

    decisions = router["decision_sequence"]
    rules = router["selection_rules"]
    assert [item["id"] for item in decisions] == [f"R{i}" for i in range(15)]
    assert [item["id"] for item in rules] == [f"SR{i:02}" for i in range(1, 8)]
    assert len(router["selection_proposal"]["fields"]) == 6

    known_codes = {entry["code"] for entry in PROCEDURE_DEFINITIONS}
    for decision in decisions:
        assert set(re.findall(r"\bP\d{2}\b", decision["route"])) <= known_codes

    assert list(protocol["ledger"]["fields"]) == [
        "request",
        "procedure",
        "control_state",
        "mandate_state",
        "mandate_summary",
        "outcome",
        "evidence_refs",
        "open_decisions",
        "assumptions",
        "next_step",
    ]
    assert [state["id"] for state in protocol["states"]] == [f"S{i}" for i in range(8)]
    assert protocol["mandate_states"] == [
        "proposed",
        "approved",
        "suspended",
        "revoked",
        "concluded",
    ]


def test_guide_reporting_policy() -> None:
    guide = _load_procedure_yaml(_decode_asset((PROCEDURES_DIR / "00-guide.yaml").read_bytes()))
    policy = guide["protocol"]["ledger"]["display_policy"]
    assert policy["default_view"] == "concise"
    assert policy["full_record_when"] == [
        "explicit_user_request",
        "necessary_audit",
        "necessary_handoff",
    ]
    assert set(policy["events"]) == {
        "opening",
        "ordinary_progress",
        "material_decision",
        "scope_change",
        "blockage_or_suspension",
        "resumption",
        "procedure_change",
        "objective_closure",
    }
    assert all(isinstance(rule, str) and rule.strip() for rule in policy["events"].values())


def test_guide_entry_is_concise_version_17() -> None:
    raw = (PROCEDURES_DIR / "00-guide.yaml").read_bytes()
    guide = _load_procedure_yaml(_decode_asset(raw))
    assert guide["meta"]["version"] == "1.7"
    assert "catalog" not in guide["router"]
    assert len(raw) <= 24 * 1024


@pytest.mark.parametrize(
    "text",
    ["version: '1.0'\nversion: '1.1'\n", "modes:\n  read: first\n  read: second\n"],
)
def test_procedure_yaml_rejects_duplicate_keys(text: str) -> None:
    """Duplicate keys must not silently replace metadata or mode definitions."""
    with pytest.raises(ValueError, match="Duplicate YAML key"):
        _load_procedure_yaml(text)


@pytest.mark.parametrize("raw", [b"\xef\xbb\xbfid: P04\n", b"id: P04\r\n"])
def test_asset_rejects_bom_and_cr(raw: bytes) -> None:
    """BOM and CR must fail even when the byte stream decodes as UTF-8."""
    with pytest.raises(ValueError):
        _decode_asset(raw)


@pytest.mark.parametrize("defect", ["version", "id", "modes", "step", "guide"])
def test_procedure_asset_rejects_invalid_structure(defect: str) -> None:
    """Reject broken revision metadata, absent modes, duplicate steps and guide blocks."""
    file_name = "00-guide.yaml" if defect == "guide" else "04-mandate-clarification.yaml"
    data = _load_procedure_yaml((PROCEDURES_DIR / file_name).read_text(encoding="utf-8"))
    if defect in {"version", "id"}:
        data[defect] = "invalid"
    elif defect == "modes":
        data["mandate_and_approval"]["modes"] = {}
    elif defect == "step":
        data["procedure"][1]["step"] = 1
    else:
        del data["router"]
    with pytest.raises(ValueError):
        _validate_procedure_asset(yaml.safe_dump(data).encode("utf-8"), file_name)


def test_file_counts() -> None:
    """Verifies that exactly 21 YAML files and 4 Markdown instruction files exist."""
    yaml_files = sorted(p.name for p in PROCEDURES_DIR.glob("*.yaml"))
    assert len(yaml_files) == 21, f"Expected 21 procedure YAML files, found {len(yaml_files)}"

    md_files = sorted(p.name for p in INSTRUCTIONS_DIR.glob("*.md"))
    assert len(md_files) == 4, f"Expected 4 instruction Markdown files, found {len(md_files)}"


@pytest.mark.parametrize("file_name,expected_meta", PROCEDURE_EXPECTED_HASHES.items())
def test_procedure_yaml_integrity(file_name: str, expected_meta: tuple[int, str]) -> None:
    """Verifies procedure structure, metadata, encoding, size and exact SHA-256."""
    expected_size, expected_sha256 = expected_meta
    file_path = PROCEDURES_DIR / file_name

    assert file_path.is_file(), f"Procedure file missing: {file_path}"

    raw_bytes = file_path.read_bytes()
    _validate_procedure_asset(raw_bytes, file_name)
    assert len(raw_bytes) == expected_size, (
        f"{file_name}: expected size {expected_size}, got {len(raw_bytes)}"
    )
    assert len(raw_bytes) <= MAX_FILE_SIZE_BYTES, (
        f"{file_name} exceeds maximum allowed size {MAX_FILE_SIZE_BYTES}"
    )

    computed_sha256 = hashlib.sha256(raw_bytes).hexdigest()
    assert computed_sha256 == expected_sha256, (
        f"{file_name}: SHA-256 mismatch.\nExpected: {expected_sha256}\nComputed: {computed_sha256}"
    )


@pytest.mark.parametrize("file_name,expected_meta", INSTRUCTION_EXPECTED_HASHES.items())
def test_instruction_markdown_integrity(file_name: str, expected_meta: tuple[int, str]) -> None:
    """Verifies each instruction Markdown exists, is under size limit, and matches SHA-256."""
    expected_size, expected_sha256 = expected_meta
    file_path = INSTRUCTIONS_DIR / file_name

    assert file_path.is_file(), f"Instruction file missing: {file_path}"

    raw_bytes = file_path.read_bytes()
    _decode_asset(raw_bytes)
    assert len(raw_bytes) == expected_size, (
        f"{file_name}: expected size {expected_size}, got {len(raw_bytes)}"
    )
    assert len(raw_bytes) <= MAX_FILE_SIZE_BYTES, (
        f"{file_name} exceeds maximum allowed size {MAX_FILE_SIZE_BYTES}"
    )

    computed_sha256 = hashlib.sha256(raw_bytes).hexdigest()
    assert computed_sha256 == expected_sha256, (
        f"{file_name}: SHA-256 mismatch.\nExpected: {expected_sha256}\nComputed: {computed_sha256}"
    )
