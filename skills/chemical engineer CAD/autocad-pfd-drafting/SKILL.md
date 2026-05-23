---
name: autocad-pfd-drafting
description: Draft and revise AutoCAD process flow diagrams (PFDs) for chemical/process engineering using the configured AutoCAD MCP server. Use when the user asks to create, edit, check, or export a process flow diagram, process equipment train, material/energy balance drawing, equipment tags, major process lines, stream labels, or PFD-style block/process diagrams in AutoCAD.
---

# AutoCAD PFD Drafting

## Core Workflow

Use the configured `autocad-mcp` server as the execution layer whenever AutoCAD drafting is requested. Prefer real AutoCAD `file_ipc` backend when available; fall back to DXF generation only when the user accepts headless output.

1. Establish scope: new drawing, revise existing drawing, or produce a DXF/PDF deliverable.
2. Gather minimum process inputs: equipment list, stream list, flow direction, main operating conditions, and requested title/block scale. If data is missing, draw placeholders marked `TBD` instead of inventing values.
3. Load the PFD drafting reference only when needed: `references/pfd-rules.md`.
4. Set layers before geometry: equipment, major process lines, minor process lines, utilities, text, tags, instruments, dimensions, notes, and title block.
5. Draft from left to right along the dominant process flow. Keep major equipment centered on a clean horizontal/vertical grid.
6. Add stream arrows, stream numbers, equipment tags, operating-condition callouts, and a compact notes/table area.
7. Run a final visual and semantic QA pass before saving or exporting.

## AutoCAD MCP Use

Start with `system(operation="status")` or equivalent status check. If the backend is not `file_ipc`, tell the user whether AutoCAD is not reachable or whether the task will be created headlessly.

Use these MCP tool groups:

- `layer`: create and set drafting layers.
- `entity`: create lines, polylines, rectangles, circles, arrows, and equipment envelopes.
- `annotation`: create text, leaders, and dimensions.
- `block`: insert repeated equipment or title-block elements if available.
- `drawing`: open, save, save as DXF, plot PDF, purge.
- `view`: zoom extents and capture screenshots for verification.

For PFDs, keep geometry simple and intelligible. Do not over-detail piping internals; save valve-by-valve logic for P&ID work.

## Drafting Priorities

- Make flow direction unmistakable.
- Make equipment tags and stream labels readable at plotting scale.
- Keep process lines orthogonal unless the user requests a sketch style.
- Separate process, utility, recycle, and waste streams by line type or layer.
- Keep text outside equipment outlines and avoid crossing leaders.
- Put unknown process values in a clear `TBD` table instead of hiding gaps.

## QA Checklist

Before finishing, check:

- All major equipment has a unique tag.
- All major streams have direction arrows.
- Stream labels are not duplicated unless they intentionally represent the same stream.
- No important process line terminates in empty space.
- Text height and line spacing are consistent.
- The drawing is zoomed to extents and saved to the requested path or an obvious project path.

## References

Read `references/pfd-rules.md` for layer names, tag conventions, layout heuristics, and a PFD-specific checklist.
