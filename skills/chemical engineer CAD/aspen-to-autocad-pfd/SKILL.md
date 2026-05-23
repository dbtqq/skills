---
name: aspen-to-autocad-pfd
description: Convert Aspen Plus or Aspen HYSYS exported simulation results into AutoCAD PFD drafting inputs, then coordinate drawing through AutoCAD MCP and the autocad-pfd-drafting skill. Use when the user provides Aspen/HYSYS reports, Excel/CSV stream summaries, block/unit operation summaries, composition tables, heat/utility summaries, or asks to turn simulation results into a process flow diagram (PFD), equipment/stream list, or AutoCAD drawing.
---

# Aspen To AutoCAD PFD

## Role

Use this skill as the upstream translator and coordinator for simulation-to-drawing work. It is not a replacement for `autocad-pfd-drafting`; it prepares reliable process data and then delegates the actual AutoCAD drafting behavior to that skill and `autocad-mcp`.

## Workflow

1. Identify inputs:
   - Aspen Plus/HYSYS exported `.xlsx`, `.csv`, `.txt`, `.rep`, or similar report files.
   - Treat native `.bkp`, `.apw`, `.apwz`, or HYSYS case files as second-stage automation only; ask for exported reports/tables if direct parsing is not practical.
2. Extract tables:
   - For spreadsheets, use structured spreadsheet tooling and preserve sheet/table names.
   - For text reports, locate stream summaries, block summaries, composition tables, and equipment result sections.
3. Normalize names and units:
   - Preserve Aspen stream/block IDs exactly as source identifiers.
   - Add engineering tags only when the user provides a tag convention or when a clear draft placeholder is needed.
   - Keep source units and add normalized units when safely convertible.
4. Build PFD JSON:
   - Use the schema in `references/pfd-json-schema.md`.
   - Populate equipment, streams, connections, stream conditions, compositions, duties, assumptions, and open items.
5. Validate:
   - Run `scripts/validate_pfd_json.py <json-file>` when a JSON artifact is produced.
   - Fix missing required fields or explicitly record unknowns in `open_items`.
6. Draft:
   - Trigger/use `autocad-pfd-drafting` for AutoCAD layout and drafting.
   - Use `autocad-mcp` for the actual AutoCAD operations.

## Delegation Boundary

This skill owns:

- Reading Aspen/HYSYS exports.
- Detecting stream and block data.
- Inferring or preserving process topology.
- Creating a clean, auditable PFD JSON input.
- Listing assumptions and missing data.

`autocad-pfd-drafting` owns:

- PFD layer conventions.
- Equipment placement and line routing.
- AutoCAD annotations and drafting QA.
- Saving/exporting DWG/DXF/PDF through `autocad-mcp`.

## Data Quality Rules

- Do not invent temperatures, pressures, flow rates, compositions, duties, equipment sizes, or connections.
- If a table says a value is missing, blank, trace, or not converged, keep that status visible.
- If units are ambiguous, preserve the original text and mark the normalized value as unknown.
- If connection topology cannot be reliably inferred, produce a stream/equipment table and ask for or mark missing endpoints.
- Keep simulation block names separate from drawing equipment tags when both exist.

## References

Read these files only when needed:

- `references/pfd-json-schema.md`: canonical intermediate JSON structure.
- `references/aspen-export-mapping.md`: common Aspen Plus/HYSYS export table names, field aliases, and inference rules.

## Useful Commands

Validate a produced JSON file:

```powershell
python C:\Users\Lenovo\.codex\skills\aspen-to-autocad-pfd\scripts\validate_pfd_json.py path\to\pfd.json
```

After validation, continue with the phrase or internal intent:

```text
Use autocad-pfd-drafting with this PFD JSON and draw it through autocad-mcp.
```
