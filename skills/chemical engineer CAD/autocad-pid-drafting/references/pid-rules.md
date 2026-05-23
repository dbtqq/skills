# P&ID Drafting Rules

## Suggested Layers

Use existing project layers if present. Otherwise create these:

- `PID-EQUIP`: equipment outlines.
- `PID-PIPE-MAJOR`: main process piping.
- `PID-PIPE-MINOR`: vents, drains, samples, bypasses.
- `PID-UTILITY`: utility piping.
- `PID-VALVE`: manual and specialty valves.
- `PID-INSTR`: instrument bubbles and field devices.
- `PID-SIGNAL`: pneumatic/electric/software signal lines.
- `PID-TAGS`: equipment, line, valve, and instrument tags.
- `PID-NOTES`: notes, holds, revision clouds.
- `PID-TIEIN`: battery limits and tie-ins.

## Line Number Pattern

Use the project pattern if given. If absent, use a readable placeholder:

`<NPS>-<SERVICE>-<SEQUENCE>-<SPEC>`

Examples: `2"-CW-101-CS`, `DN50-HCl-203-PTFE`, `4"-STEAM-015-A1`.

Do not invent pipe spec, material, insulation, heat tracing, or service codes when missing. Mark them `TBD`.

## Tags

Common equipment tags:

- Pumps: `P-101A/B`
- Vessels: `V-101`
- Tanks: `T-101`
- Heat exchangers: `E-101`
- Columns: `C-101`
- Reactors: `R-101`

Common instrument tags:

- Flow: `FE`, `FT`, `FI`, `FIC`, `FV`
- Pressure: `PT`, `PI`, `PIC`, `PSV`
- Temperature: `TE`, `TT`, `TI`, `TIC`
- Level: `LT`, `LI`, `LIC`, `LSH`, `LSL`

Use the user's tag list as authority when provided.

## Symbol and Connectivity Guidance

- Put valves on the line they control; align their center with the pipe centerline.
- Place instruments near the measured/controlled point and connect with signal lines.
- Use flow arrows on all non-obvious lines.
- Avoid ambiguous pipe crossings. Add spacing, line breaks, or jump marks when needed.
- Show drains, vents, samples, relief paths, and bypasses only when provided or clearly requested.

## Safety and Engineering Caution

Never fabricate relief devices, interlocks, alarms, shutdown logic, setpoints, or hazardous service details. Ask or mark `TBD` when missing. P&IDs are safety-relevant documents.

## Final Checks

- Line numbers placed at reasonable intervals.
- Valve and instrument tags unique.
- Equipment nozzles have clear pipe connections.
- Control loops have matching tags across devices and signals.
- Battery limits and tie-ins are labeled.
- Revision or hold notes are visible when the drawing contains assumptions.
