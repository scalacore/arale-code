# Cross-Platform Rules

This document specifies the operational rules for `arale-code` across macOS, Linux, and Windows environments.

## 1. Line Endings and File Encodings

- **File Encoding**: All source code, YAML manifests, Markdown instructions, and JSON configuration files must use UTF-8 encoding without a Byte Order Mark (BOM).
- **Line Endings**: All files in the repository must use line feed (LF, `0x0A`) line endings. Carriage return characters (CR, `0x0D`) must not be committed to the repository or emitted in runtime outputs.
- **Git Normalization**: `.gitattributes` must enforce `text=auto eol=lf`, `*.yaml text eol=lf`, and `*.md text eol=lf` to ensure line endings remain uniform on Windows checkouts.
- **Hash Stability**: All SHA-256 asset checksums must be computed over raw file bytes using LF line endings. Checksum validation must read raw bytes directly without platform newline conversions.

## 2. Path Handling

- **Internal Paths**: All package resource lookups must use Python standard library `importlib.resources.files` to remain agnostic of filesystem path separators.
- **External Path Formats**: Path separators within JSON configuration files and YAML manifests must use POSIX forward slashes (`/`).
- **Windows Backslash Rules**: When backslashes are used on Windows in JSON or TOML configurations, backslashes must be escaped (`\\\\`). Single-quoted TOML strings or forward slashes must be preferred.
- **Process Spawning**: Subprocess commands and arguments must be passed as argument lists (`list[str]`), avoiding platform shell interpreters and shell word-splitting.

## 3. Resolving the `uv` Executable

- **Interactive Shell Context**: When launched from an interactive terminal session on macOS, Linux, or Windows, the client inherits user `PATH` entries where `uv` resides (`~/.cargo/bin`, `~/.local/bin`, or `/opt/homebrew/bin`).
- **GUI Application Context**: When launched from desktop environments or system managers without shell inheritance, the client starts with a minimal default system `PATH`.
- **Resolution Strategy**: Client configurations must resolve `uv` using one of the following methods:
  1. Rely on full executable path (`/Users/<user>/.cargo/bin/uv` or `C:\Users\<user>\.cargo\bin\uv.exe`).
  2. Launch the host editor or agent from the terminal (`cursor .`, `codex`, `claude`).
  3. Symlink `uv` to a system path directory such as `/usr/local/bin/uv`.

## 4. Client Restart and Reload Rules

- **Static JSON/TOML Configurations**: Modifications to `mcp.json`, `config.toml`, `.mcp.json`, or `opencode.json` require restarting the client application or ending the active session before new server definitions take effect.
- **Dynamic CLI Additions**: When registered via native CLI commands (`claude mcp add`, `codex mcp add`, `agent mcp add`, `opencode mcp add`), configuration changes are applied immediately to subsequent session launches.
- **Session Isolation**: Each STDIO process spawned by a client is isolated to the lifecycle of that client session. Server termination must release standard file descriptors without hanging.
