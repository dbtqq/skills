#!/usr/bin/env python3
"""Validate the minimal Aspen-to-PFD intermediate JSON shape."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_TOP_LEVEL = ("metadata", "equipment", "streams", "connections", "open_items")
REQUIRED_EQUIPMENT = ("id", "type")
REQUIRED_STREAM = ("id", "type")
REQUIRED_CONNECTION = ("stream_id", "from", "to")


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def require_keys(obj: dict, keys: tuple[str, ...], where: str) -> list[str]:
    return [f"{where}: missing key '{key}'" for key in keys if key not in obj]


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        return fail("usage: validate_pfd_json.py <pfd.json>")

    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return fail(f"cannot read JSON: {exc}")

    errors: list[str] = []
    if not isinstance(data, dict):
        return fail("top-level JSON value must be an object")

    errors.extend(require_keys(data, REQUIRED_TOP_LEVEL, "top-level"))

    for key in ("equipment", "streams", "connections", "open_items"):
        if key in data and not isinstance(data[key], list):
            errors.append(f"top-level '{key}' must be a list")

    for idx, item in enumerate(data.get("equipment", [])):
        if not isinstance(item, dict):
            errors.append(f"equipment[{idx}] must be an object")
            continue
        errors.extend(require_keys(item, REQUIRED_EQUIPMENT, f"equipment[{idx}]"))

    for idx, item in enumerate(data.get("streams", [])):
        if not isinstance(item, dict):
            errors.append(f"streams[{idx}] must be an object")
            continue
        errors.extend(require_keys(item, REQUIRED_STREAM, f"streams[{idx}]"))

    stream_ids = {item.get("id") for item in data.get("streams", []) if isinstance(item, dict)}
    equipment_ids = {item.get("id") for item in data.get("equipment", []) if isinstance(item, dict)}
    sentinel_ids = {"FEED", "PRODUCT", "WASTE", "UTILITY", "UNKNOWN"}

    for idx, item in enumerate(data.get("connections", [])):
        if not isinstance(item, dict):
            errors.append(f"connections[{idx}] must be an object")
            continue
        errors.extend(require_keys(item, REQUIRED_CONNECTION, f"connections[{idx}]"))
        stream_id = item.get("stream_id")
        if stream_id and stream_id not in stream_ids:
            errors.append(f"connections[{idx}]: stream_id '{stream_id}' not found in streams")
        for end_key in ("from", "to"):
            endpoint = item.get(end_key)
            if endpoint and endpoint not in equipment_ids and endpoint not in sentinel_ids:
                errors.append(
                    f"connections[{idx}]: {end_key} endpoint '{endpoint}' is not equipment or sentinel"
                )

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("PFD JSON is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
