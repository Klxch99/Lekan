Purpose
- Help AI coding agents work productively in this repository: a small, local data exploration project focused on a US vehicles dataset.

Quick Context
- Primary artifacts: `Notebooks/eda.ipynb` (main analysis), `vehicles_us.csv.csv` (local dataset), `app.py` (placeholder), `README.md`.
- The notebook reads the CSV using an absolute Windows path (see first cell). Many edits will involve the notebook JSON rather than pure .py files.

Big Picture / Architecture
- Single-repo data-analysis project: source-of-truth is the CSV and the Jupyter notebook. There is no service or web backend.
- Data flow: `Notebooks/eda.ipynb` reads `vehicles_us.csv.csv`, performs cleaning (filter price/odometer, impute `model_year`, `cylinders` by `type`, fill `paint_color`, etc.), computes derived columns (`vehicle_age`, `price_per_mile`, `log_price`, `posting_month`), and produces Plotly figures.

Key files to inspect first
- Notebooks/eda.ipynb — canonical analysis and visualization code (preserve cell structure/IDs when possible).
- vehicles_us.csv.csv — large local CSV (do not overwrite or rename without asking).
- app.py — currently empty; if adding scripts, prefer creating small helpers (e.g., `scripts/`) and a `requirements.txt`.

Project-specific patterns & conventions
- Notebook-first workflow: edits are often in-place in `Notebooks/eda.ipynb`.
- Data loading currently uses an absolute Windows path (r"C:\Users\olale\Documents\Lekan\vehicles_us.csv.csv"). When updating code, prefer adding a configurable, relative path or `os.path` logic rather than changing the dataset filename.
- Imputation pattern: `model_year` uses dataset median; `cylinders` uses group median via `df.groupby('type')['cylinders'].transform(...)` — preserve this approach unless there is a clear improvement.
- Plotting: `plotly.express` is used; figures are adjusted with `fig.update_layout(...)` for axis ranges and then `fig.show()`.
- Data filters: repo filters out `price < 100` and `odometer > 400_000` early; keep these guardrails unless creating an alternate experimental branch.

Developer workflows / commands
- Environment (recommended): create a venv and install core libs:

  python -m venv .venv
  .venv\Scripts\pip install --upgrade pip
  .venv\Scripts\pip install pandas numpy plotly jupyter

- Run notebooks: open `Notebooks/eda.ipynb` in VS Code or run `jupyter notebook` and execute cells.
- If adding Python scripts, include `requirements.txt` with pinned versions and prefer `black` for formatting.

When editing notebooks
- Keep `metadata.id` fields for existing cells intact. New cells may omit `id` but avoid reordering or deleting many cells without reason.
- Use the provided Notebook JSON format conventions (cells must have `metadata.language`).
- For programmatic edits, prefer creating new `.py` scripts under `scripts/` and exporting results into new notebooks or artifacts instead of wholesale rewriting `eda.ipynb`.

Integration points & constraints
- No external APIs or services are present. The main constraint is local memory when loading the CSV — prefer streaming/chunking for heavy operations if you add larger transforms.
- File paths are Windows-style; be careful with path separators and raw-string literals (r"...").

Examples of safe agent tasks
- Replace the absolute CSV path in `Notebooks/eda.ipynb` with a small cell that sets a relative `DATA_PATH` and documents how to override it.
- Add a `requirements.txt` listing `pandas,numpy,plotly,jupyter`.
- Add a lightweight `scripts/convert_notebook.py` that converts `eda.ipynb` to HTML for sharing.

What to avoid
- Do not modify or delete `vehicles_us.csv.csv`.
- Avoid large, opinionated refactors of the notebook content without opening an issue first.

If something is unclear
- Ask the repo owner before renaming files or changing the data-loading path. Prefer creating a small PR that documents changes in the PR description.

Next steps for contributors
- Check out `Notebooks/eda.ipynb` and open a small PR for any change that alters dataset loading or core cleaning steps.

If you'd like changes to these instructions, tell me which areas need more detail (examples: environment pins, notebook editing rules, or preferred commit messages).
