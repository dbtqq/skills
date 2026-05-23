---
name: autocad-pid-drafting
description: Draft and revise AutoCAD piping and instrumentation diagrams (P&IDs/PIDs) for process plants using the configured AutoCAD MCP server. Use when the user asks to create, edit, check, or export P&ID drawings, piping lines, line numbers, valves, pumps, vessels, tanks, instruments, control loops, interlocks, utility tie-ins, or ISA-style process instrumentation diagrams in AutoCAD.
---

# AutoCAD P&ID Drafting

## Core Workflow

Use the configured `autocad-mcp` server as the execution layer. Prefer the MCP `pid` operations when they fit the request, then use general `entity`, `layer`, `block`, and `annotation` operations for custom detailing.

1. Establish drawing scope: new P&ID, partial loop, equipment package, or revision to an existing DWG/DXF.
2. Gather minimum inputs: equipment tags, line list, valve list, instrument list, control loop intent, utilities, battery limits, and revision status. Mark unknown values as `TBD`.
3. Load `references/pid-rules.md` when detailed symbol, line-number, or QA guidance is needed.
4. Set up layers first. Use the MCP `pid.setup_layers` operation if available.
5. Place major equipment before piping. Route main process lines, then utility/vent/drain/sample lines.
6. Add valves, instruments, line numbers, flow arrows, equipment tags, notes, and tie-in markers.
7. Check connectivity and tag consistency before saving/exporting.

## AutoCAD MCP Use

Start with `system(operation="status")`. If AutoCAD is not reachable, explain that true P&ID editing needs the `file_ipc` backend unless the user only wants a headless DXF.

Prefer these `pid` operations when available:

- `setup_layers`
- `insert_symbol`
- `draw_process_line`
- `connect_equipment`
- `add_flow_arrow`
- `add_equipment_tag`
- `add_line_number`
- `insert_valve`
- `insert_instrument`
- `insert_pump`
- `insert_tank`

Use generic tools for gaps:

- `entity` for custom piping geometry and simple symbols.
- `annotation` for tag bubbles, notes, and leaders.
- `block` for repeated symbols if a block library is present.
- `drawing` for open/save/export/purge.
- `view` for screenshots and visual verification.

## Drafting Priorities

- Treat line numbers, valve tags, equipment tags, and instrument tags as controlled identifiers.
- Do not invent safety devices, control functions, setpoints, or interlocks. Use `TBD` or ask when the omission affects process safety or drawing meaning.
- Keep piping connectivity legible. Avoid ambiguous crossings; use line jumps or spacing.
- Use P&ID detail level: valves, instruments, reducers, drains, vents, samples, spectacle blinds, strainers, and tie-ins when provided.
- Keep symbol style consistent within a drawing, even if the available library is limited.

## QA Checklist

Before finishing, check:

- Each line segment has a line number or an intentional continuation.
- Each equipment item has a unique tag.
- Valves and instruments are attached to the correct line or equipment.
- Flow arrows match the process intent.
- Instrument loop tags are consistent across bubbles, signals, and notes.
- Crossings are visually unambiguous.
- Title block/revision notes reflect the user's request when provided.

## References

Read `references/pid-rules.md` for layer conventions, tag formats, P&ID symbol guidance, line-number patterns, and QA rules.
