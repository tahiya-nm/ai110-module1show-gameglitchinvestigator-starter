# Refactor Agent Memory — Game Glitch Investigator

## Project Structure
- `app.py` — Streamlit UI only. All business logic has been moved to `logic_utils.py`.
- `logic_utils.py` — Contains all four pure logic functions. No Streamlit imports.

## Module Organization Convention
- Pure logic functions belong in `logic_utils.py` (no Streamlit imports there).
- Presentation/UI code stays in `app.py`.
- Import style used: `from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score` (explicit named imports, not `import logic_utils`).

## Refactor Pattern for This Repo
- `logic_utils.py` originally contained stub functions with `raise NotImplementedError(...)` as placeholders.
- To move a function: replace the stub body in `logic_utils.py` with the real implementation, then remove the definition from `app.py`, then add/extend the `from logic_utils import ...` line in `app.py`.
- Do NOT duplicate stubs — replace them in place so docstrings are preserved.

## All Functions Now in logic_utils.py (Refactor Complete)
- `parse_guess` — moved from `app.py`
- `check_guess` — moved from `app.py`
- `get_range_for_difficulty` — moved from `app.py`
- `update_score` — moved from `app.py`

## Remaining Known Bugs in app.py (not yet fixed)
- History logging bug: on a failed parse, `raw_guess` (old input) is appended to history instead of the current input. Marked with a FIXME comment at line 91.
