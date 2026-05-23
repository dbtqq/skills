# PFD JSON Schema

Use this as the canonical intermediate format between Aspen/HYSYS exports and AutoCAD drafting.

## Top-Level Object

Required keys:

- `metadata`: source and project context.
- `equipment`: list of process blocks/equipment.
- `streams`: list of material, energy, or utility streams.
- `connections`: explicit from/to topology.
- `open_items`: assumptions, missing values, and unresolved mapping issues.

Optional keys:

- `tables`: extracted raw table summaries.
- `layout_hints`: preferred drawing order, grouping, or manual positioning hints.
- `notes`: drawing notes to carry into the PFD.

## Example

```json
{
  "metadata": {
    "source": "Aspen Plus stream_summary.xlsx",
    "simulator": "Aspen Plus",
    "case_name": "TBD",
    "unit_basis": "as exported"
  },
  "equipment": [
    {
      "id": "PUMP1",
      "tag": "P-101",
      "type": "pump",
      "name": "Feed Pump",
      "source_block_type": "PUMP",
      "parameters": {
        "power_kW": 12.4,
        "pressure_increase_kPa": 350
      }
    }
  ],
  "streams": [
    {
      "id": "S1",
      "type": "material",
      "name": "Feed",
      "conditions": {
        "temperature_C": 25,
        "pressure_kPa": 101.3,
        "mass_flow_kg_h": 1000,
        "molar_flow_kmol_h": null,
        "vapor_fraction": 0
      },
      "composition": {
        "WATER": {"mole_fraction": 0.8},
        "METHANOL": {"mole_fraction": 0.2}
      }
    }
  ],
  "connections": [
    {"stream_id": "S1", "from": "FEED", "to": "PUMP1", "role": "feed"}
  ],
  "open_items": [
    "Equipment tags are draft placeholders unless user supplies project tag list."
  ]
}
```

## Equipment Fields

Required:

- `id`: Aspen/HYSYS block name or stable extracted identifier.
- `type`: normalized type such as `pump`, `compressor`, `heater`, `heat_exchanger`, `reactor`, `column`, `flash`, `separator`, `mixer`, `splitter`, `tank`, `valve`, `unknown`.

Recommended:

- `tag`: drawing tag. Use `TBD` or placeholder when not supplied.
- `name`: human-readable name.
- `source_block_type`: simulator block type.
- `parameters`: duties, pressure changes, stage counts, reflux ratio, work, efficiencies, or other block results.

## Stream Fields

Required:

- `id`: Aspen/HYSYS stream ID.
- `type`: `material`, `energy`, `utility`, or `unknown`.

Recommended:

- `name`: service name if known.
- `conditions`: normalized key-value values with units in key names where practical.
- `composition`: component map by mole/mass fraction, flow, or concentration.
- `phase`: vapor/liquid/solid/mixed if known.

## Connection Fields

Required:

- `stream_id`
- `from`
- `to`

Use sentinel endpoints when needed:

- `FEED`
- `PRODUCT`
- `WASTE`
- `UTILITY`
- `UNKNOWN`

Record every `UNKNOWN` endpoint in `open_items`.
