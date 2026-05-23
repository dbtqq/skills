# Equipment Condition Drawing Rules

## Suggested Layers

Use existing project layers if present. Otherwise create these:

- `ECD-OUTLINE`: visible equipment outline.
- `ECD-HIDDEN`: hidden edges.
- `ECD-CENTER`: centerlines and datums.
- `ECD-NOZZLE`: nozzles, flanges, connection points.
- `ECD-SUPPORT`: saddles, skirts, legs, baseplates, anchor points.
- `ECD-DIM`: dimensions and extension lines.
- `ECD-TEXT`: notes and labels.
- `ECD-TABLE`: nozzle table and condition table.
- `ECD-MAINT`: maintenance/removal envelope.
- `ECD-TBD`: holds, unknown dimensions, open interfaces.

## View Selection

- Horizontal vessel: elevation plus plan; add end view when nozzle orientation matters.
- Vertical vessel/column: elevation plus plan/nozzle orientation view.
- Tank: plan plus elevation; show manholes, nozzles, vents, overflow, drain.
- Heat exchanger: elevation plus nozzle/end orientation view.
- Pump/compressor: plan plus elevation; show baseplate, suction/discharge, motor envelope, maintenance pull space.
- Skid/package: plan view first, elevation if interfaces or heights matter.

## Nozzle Table Fields

Use a table when there are more than three nozzles. Suggested columns:

- Nozzle tag
- Service
- Size/rating/facing
- Orientation or angle
- Elevation or centerline height
- Projection
- Connection type
- Remarks/status

Mark missing values as `TBD`; do not leave blank cells that look confirmed.

## Dimension Rules

- Dimension from equipment centerline, tangent line, bottom of baseplate, finished floor, or other stable datum.
- Show overall length/width/height.
- Show nozzle centerline locations and elevations.
- Show support spacing, anchor-bolt pattern, and foundation interface when provided.
- Show maintenance/removal envelopes as dashed or separate-layer outlines.

## Coordination Notes

Typical condition notes may include:

- All dimensions are preliminary unless marked certified.
- Nozzle orientation to be confirmed by vendor.
- Foundation loads by mechanical/vendor data.
- Maintenance clearance to be reserved by layout.
- Interface dimensions marked `TBD` require confirmation before issue.

## Final Checks

- Equipment tag, service, and drawing purpose visible.
- Views align with each other.
- Nozzle tags in graphics match the table.
- Datums and centerlines are present.
- `TBD` values are obvious.
- Maintenance envelope and support/foundation interfaces do not conflict.
