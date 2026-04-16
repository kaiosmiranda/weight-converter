# weight-converter

A Python command-line tool that converts weight between kilograms and pounds.

## Usage

```bash
python3 app.py
```

Example:

```
Weight: 170
(K)g or (L)bs: l
Weight in Kg: 76.5
```

## Accepted inputs

| Input | Meaning | Output |
|-------|---------|--------|
| `k` or `K` | Value is in lbs | Converts to kg |
| `l` or `L` | Value is in kg | Converts to lbs |

## Formulas

- **lbs → kg:** `weight × 0.450`
- **kg → lbs:** `weight ÷ 0.450`

## Concepts applied

- Variables and data types
- Type conversion (`float`)
- User input (`input`)
- String normalization (`.lower()`)
- Conditionals (`if / elif / else`)

## Planned improvements

- [ ] Error handling for invalid inputs (`try/except`)
- [ ] Support for additional units (grams, tonnes)
- [ ] Command-line arguments (`argparse`)

## Status

`v1.0` — functional. Improvements planned as Python studies progress.