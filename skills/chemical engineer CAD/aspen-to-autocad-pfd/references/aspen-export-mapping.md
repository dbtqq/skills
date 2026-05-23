# Aspen/HYSYS Export Mapping

Use source table names and headings as clues. Preserve raw extracted values when uncertain.

## Common Table Names

Aspen Plus:

- `Stream Summary`
- `Material Stream Summary`
- `Block Summary`
- `Results Summary`
- `Composition`
- `Mole Flow`
- `Mass Flow`
- `Properties`
- `Unit Operation Results`

Aspen HYSYS:

- `Workbook`
- `Material Streams`
- `Energy Streams`
- `Unit Ops`
- `Stream Conditions`
- `Composition`
- `Worksheet`

## Field Aliases

Stream ID:

- `Stream`
- `Stream ID`
- `Name`
- `Material Stream`

Block/equipment ID:

- `Block`
- `Block ID`
- `Unit Operation`
- `Operation`
- `Name`

Temperature:

- `Temperature`
- `TEMP`
- `T`
- `Temp`

Pressure:

- `Pressure`
- `PRES`
- `P`
- `Press`

Flow:

- `Mass Flow`
- `MASSFLOW`
- `Molar Flow`
- `MOLEFLOW`
- `Std Liq Vol Flow`
- `Volume Flow`

Composition:

- Component names as columns.
- Rows labelled `Mole Frac`, `Mass Frac`, `Mole Flow`, or `Mass Flow`.

## Block Type Normalization

- `PUMP` -> `pump`
- `COMPRESSOR`, `COMPR` -> `compressor`
- `HEATER`, `COOLER` -> `heater`
- `HEATX`, `MHEATX`, `LNG` exchanger blocks -> `heat_exchanger`
- `FLASH2`, `FLASH3`, `SEP`, `SEPARATOR` -> `separator`
- `RADFRAC`, `DISTL`, `COLUMN` -> `column`
- `RCSTR`, `RPLUG`, `RSTOIC`, `REQUIL`, `RGIBBS` -> `reactor`
- `MIXER` -> `mixer`
- `FSPLIT`, `SPLITTER` -> `splitter`
- `VALVE` -> `valve`

## Topology Inference

Prefer explicit input/output stream lists from block summaries. If absent:

1. Use stream names and block result sections that list `Input Streams` and `Output Streams`.
2. Use stream tables with `From` and `To` columns.
3. Use HYSYS workbook connections if exported.
4. If topology still cannot be inferred, create streams and equipment but set unknown endpoints in `connections`.

Do not infer topology solely from row order unless the user explicitly accepts a rough draft.

## Drawing Preparation

Before calling `autocad-pfd-drafting`, produce:

- Main process path if identifiable.
- Recycle streams.
- Utilities and energy streams.
- Product and waste streams.
- Open items for missing endpoints or ambiguous unit operations.
