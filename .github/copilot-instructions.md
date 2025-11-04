<!-- Copilot / AI agent instructions for the chenweida6220 repo -->
# Repository snapshot (what this repo is)
- Small personal portfolio that generates two SVG "namecards" (light/dark) from Python scripts.
- Key files:
  - `README.md` (root) — contains the HTML <picture> tag that references the generated SVGs.
  - `Portfolio Items/light-mode_namecard.py` — generates `light-mode_namecard.svg`.
  - `Portfolio Items/dark-mode_namecard.py` — generates `dark-mode_namecard.svg`.
  - Image assets live under `Portfolio Items/` (e.g., `*_headshot-ascii-art.png`).

# Big-picture architecture (short)
- This is not a multi-service app. The repo contains small Python scripts that produce SVG artifacts consumed directly by the README (rendered on GitHub).
- Data flow: PNG headshot -> base64-embedded into SVG by Python script -> output SVG placed at repo root -> referenced in `README.md` for both light and dark variants.

# Developer workflows (concrete commands)
- Create and activate a venv (PowerShell):
  ```powershell
  python -m venv .venv; .\.venv\Scripts\Activate.ps1
  ```
- Install runtime deps:
  ```powershell
  pip install svgwrite pytz
  ```
- Generate the SVGs (run from repo root):
  ```powershell
  python "Portfolio Items\light-mode_namecard.py"
  python "Portfolio Items\dark-mode_namecard.py"
  ```
- Expected result: `light-mode_namecard.svg` and `dark-mode_namecard.svg` appear in the repo root and are referenced by `README.md`.

# Project-specific patterns & conventions
- Filenames: snake_case with suffix `_namecard.py` for the generator scripts; final SVG filenames are exactly `light-mode_namecard.svg` and `dark-mode_namecard.svg` (README references these names — do not rename without updating README).
- Image embedding: scripts convert PNG assets into base64 data URIs and embed them into the SVG (see `data_uri` construction). This is deliberate so GitHub will render the image inside the SVG without external references.
- Timestamping: the scripts use `AUTO_UPDATE = True` and `pytz.timezone("America/New_York")` to populate `LAST_LOGIN`. If you change timezone behavior, update both scripts consistently.
- Text layout: helper functions `dash_leader` and `dot_leader` build fixed-width label/value lines; preserve their signature/behavior when editing layout logic.

# Integration points & external dependencies
- Python packages: `svgwrite` and `pytz` (install with pip). The rest (base64, datetime) are stdlib.
- GitHub rendering: SVGs are intended to be displayed in `README.md` via an HTML <picture> tag. Avoid adding external image hrefs inside the SVG — prefer embedding base64 as implemented.

# Common pitfalls the AI should avoid changing
- Do not change the exact output SVG filenames without updating `README.md`.
- Do not remove the data-URI approach unless you also change README and validate GitHub rendering.
- Watch binary assets: embedding large PNGs produces large diffs; prefer using the commented alternative (store base64 in a text file and read it) if commit size is a concern.

# Helpful quick examples for edits
- To change the background color in both modes: update `BG_COLOR` at the top of each script and re-run the script.
- To disable automatic timestamps for testing: set `AUTO_UPDATE = False` and set `LAST_LOGIN` to a fixed string.
- To swap the headshot asset: replace the corresponding `Portfolio Items/*_headshot-ascii-art.png` file and re-run the generator (scripts expect those exact paths).

# When to run tests / checks (manual)
- No unit tests exist. Quick local validation is: run the scripts, open the generated SVG files in a browser, and ensure the README preview shows the correct image.

# If you need more context
- Start by opening `Portfolio Items/light-mode_namecard.py` — it contains the most explicit doc-comments about why images are base64-embedded.
- If you plan to add automation (CI) for regenerating SVGs, update this file and the `README.md` references together.

---
Please review these notes and tell me if you'd like stricter rules (e.g., linting, CI steps, or a requirements.txt) added to this guidance.
