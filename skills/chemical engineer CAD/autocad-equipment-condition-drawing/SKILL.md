---
name: autocad-equipment-condition-drawing
description: Draft and revise AutoCAD equipment condition drawings for process equipment coordination. Use when the user asks for equipment condition drawings, equipment outline drawings, nozzle orientation drawings, equipment interfaces, foundation/load conditions, maintenance envelopes, package equipment conditions, nozzle tables, equipment datasheet-to-drawing conversion, or discipline handoff drawings in AutoCAD.
---

# AutoCAD Equipment Condition Drawing

## Core Workflow

Use the configured `autocad-mcp` server as the execution layer when the user wants AutoCAD output. These drawings are coordination deliverables; prioritize clear interfaces, dimensions, orientation, and condition notes over decorative detail.

1. Establish equipment type: vessel, tank, heat exchanger, pump, compressor, skid, column, filter, or package unit.
2. Gather minimum inputs: equipment tag/name, overall dimensions, orientation, nozzle list, support/foundation requirements, maintenance clearances, weights/loads if provided, and requested view set.
3. Load `references/equipment-condition-rules.md` when detailed layout, table, or QA guidance is needed.
4. Choose views: plan, elevation, side view, nozzle orientation view, and/or detail callouts.
5. Set layers for outlines, centerlines, nozzles, dimensions, text, tables, hidden lines, maintenance envelopes, and title/revision items.
6. Draft the equipment envelope first, then centerlines, nozzles/interfaces, supports, clearances, dimensions, tables, and notes.
7. Run interface QA before saving/exporting.

## AutoCAD MCP Use

Start with `system(operation="status")`. Use these MCP tool groups:

- `layer`: create controlled drafting layers.
- `entity`: draw equipment outlines, centerlines, nozzles, supports, and clearance envelopes.
- `annotation`: create dimensions, leaders, notes, and table text.
- `block`: insert repeated nozzle, flange, support, or title-block elements if available.
- `drawing`: open, save, save as DXF, plot PDF, purge.
- `view`: zoom extents and capture verification screenshots.

If a precise manufacturer drawing or datasheet is missing, create a condition drawing with clearly marked `TBD` dimensions and interface placeholders.

## Drafting Priorities

- Show interfaces that other disciplines need: nozzles, supports, loads, envelope, maintenance clearance, lifting/handling notes, and battery-limit points.
- Keep centerlines and datum references visible.
- Dimension from stable datums, not from arbitrary graphics.
- Put nozzle information in a table when more than three nozzles exist.
- Separate "confirmed" values from `TBD` values.
- Avoid fabrication-level details unless the user asks for manufacturing drawings.

## QA Checklist

Before finishing, check:

- Equipment tag and drawing title are present.
- Required views match the equipment type and user request.
- Overall dimensions and main datums are shown.
- Nozzle tags in the view match the nozzle table.
- Maintenance envelopes do not obscure the equipment outline.
- Support/foundation points are dimensioned or marked `TBD`.
- Unknown values are visible, not silently omitted.

## References

Read `references/equipment-condition-rules.md` for view selection, layer names, nozzle table fields, dimension rules, and coordination checks.
