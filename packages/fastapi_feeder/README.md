## fastapi_feeder — development

This document shows how to run the `fastapi_feeder` package individually for development using the repository `.venv`.

Prerequisites
- Python 3.11 installed (the repository uses a `.venv` at the repo root).

Activate the repository virtualenv

```bash
# from the repo root
source .venv/bin/activate
```

Install editable package and tools

```bash
# ensure pip and build tools are available in the venv
.venv/bin/python -m ensurepip --upgrade
.venv/bin/python -m pip install --upgrade pip setuptools wheel

# install this package in editable mode so source changes are reflected immediately
.venv/bin/python -m pip install -e packages/fastapi_feeder

# (optional) install the uv CLI into the venv to run apps by name
.venv/bin/python -m pip install uv
```

Run the package

- With uv (recommended when you want `uv run fastapi_feeder`):

```bash
# run using the venv's uv so it uses the same interpreter and packages
.venv/bin/uv run fastapi_feeder
```

- Directly with Python (quick check):

```bash
.venv/bin/python -m fastapi_feeder.main
# or use the project smoke script
.venv/bin/python scripts/run_apps.py
```

Development workflow notes
- Code changes under `packages/fastapi_feeder/src/fastapi_feeder/` are picked up immediately by the editable install; just restart the running process.
- If you change packaging metadata (for example `pyproject.toml`), console scripts, or move files, reinstall editable

```bash
.venv/bin/python -m pip uninstall fastapi_feeder -y || true
.venv/bin/python -m pip install -e packages/fastapi_feeder
```

- If `uv run fastapi_feeder` fails to import the package, confirm you're using the same venv that has the package installed:

```bash
source .venv/bin/activate
python -c "import fastapi_feeder; print('fastapi_feeder ->', fastapi_feeder.__file__)"
```

Optional: auto-reload during development

For automatic restarts on file changes you can use a simple watcher (requires `entr`):

```bash
# install entr (macOS: brew install entr)
find packages/fastapi_feeder/src/fastapi_feeder -name '*.py' | entr -r .venv/bin/uv run fastapi_feeder
```

That's it — edit code in `packages/fastapi_feeder/src/fastapi_feeder/` and either restart `uv` or use a watcher to pick up changes.

