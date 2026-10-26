#!/usr/bin/env python3
"""Prepare an example ESPHome config to build the checked-out MIoT sources.

Original example YAML files are never modified. CI uses synthetic credentials.
"""

import argparse
import base64
from pathlib import Path
import re
import secrets


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
COMPONENTS = REPOSITORY_ROOT / "components"
SOURCE_RE = re.compile(
    r"(?m)^(?P<indent>[ \t]*)source:[ \t]*"
    r"github://(?:bruvv|dhewg)/esphome-miot@[^\s#]+[ \t]*(?:#.*)?$"
)

def ci_secrets() -> str:
    # Generate a fresh, valid 32-byte key per CI job, never store one in Git.
    api_key = base64.b64encode(secrets.token_bytes(32)).decode("ascii")
    return f"""# Synthetic credentials for offline CI builds only; never deploy these.
api_encryption_key: "{api_key}"
ota_password: "ci-only-ota-password"
wifi_ssid: "ESPHome-CI"
wifi_password: "ci-only-wifi-password"
wifi_ap_password: "ci-only-ap-password"
"""


def prepare(source: Path, output: Path) -> None:
    content = source.read_text(encoding="utf-8")

    def local_source(match: re.Match) -> str:
        indent = match.group("indent")
        return (
            f"{indent}source:\n"
            f"{indent}  type: local\n"
            f"{indent}  path: {COMPONENTS.as_posix()}"
        )

    updated, count = SOURCE_RE.subn(local_source, content)
    if count != 1:
        raise ValueError(
            f"Expected exactly one esphome-miot external source in {source}, got {count}"
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(updated, encoding="utf-8")
    (output.parent / "secrets.yaml").write_text(ci_secrets(), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--target", type=Path, required=True)
    args = parser.parse_args()
    prepare(args.source, args.target)


if __name__ == "__main__":
    main()
