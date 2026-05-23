# PFD Drafting Rules

## Suggested Layers

Use existing project layers if present. Otherwise create these:

- `PFD-EQUIP`: equipment outlines, color 7, continuous, medium weight.
- `PFD-PROCESS-MAJOR`: main process streams, color 1, continuous, heavy weight.
- `PFD-PROCESS-MINOR`: secondary process streams, color 3, continuous, medium weight.
- `PFD-UTILITY`: utility streams, color 5, dashed or continuous per project convention.
- `PFD-RECYCLE`: recycle lines, color 6, continuous, medium weight.
- `PFD-TEXT`: labels and notes, color 7.
- `PFD-TAGS`: equipment and stream tags, color 2.
- `PFD-INSTR`: key control indicators only, color 4.
- `PFD-TABLE`: stream table, equipment list, notes.

## Layout Heuristics

- Main process flow: left to right, top to bottom only for secondary branches.
- Place feed preparation upstream left, reactors/major units center, separation/downstream right.
- Keep pumps below or near the equipment they serve.
- Put heat exchangers near their process streams; show utility side only when relevant.
- Keep line crossings rare; prefer vertical offsets and elbows.
- Reserve right or bottom area for stream/equipment tables.

## Tag Conventions

Common equipment prefixes:

- `P`: pump
- `V`: vessel
- `T`: tank
- `E`: exchanger
- `R`: reactor
- `C`: column/compressor depending on project; clarify if ambiguous
- `F`: filter
- `M`: mixer

Use unique tags such as `P-101A/B`, `E-102`, `V-201`. Stream numbers can be `S-001`, `S-002`, or project-specific numeric labels.

## Annotation Rules

- Label each major stream with stream number and direction arrow.
- Use callouts for temperature, pressure, phase, and flow only when provided.
- Put multi-value data in a table instead of crowding the drawing.
- Use `TBD` for unknown values and keep a visible `TBD / open items` note.

## Final Checks

- Equipment tags unique.
- Stream direction arrows present.
- No text overlaps process lines.
- Major lines connect to equipment or battery-limit arrows.
- Utility and recycle streams are visually distinct.
- Drawing saved and zoomed to extents before screenshot/export.
