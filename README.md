# llmv3
llm study extended

## Creating virtual environment at: env 
```bash
uv venv env --python $(pyenv root)/versions/3.11.9/bin/python 
```

Using CPython 3.11.9 interpreter at: /Users/kamlesh/.pyenv/versions/3.11.9/bin/python

Activate env with: 
```bash
source .venv/bin/activate
```

Running locally
-----------------
After activating the virtual environment, install editable packages and uv into the venv and run the apps:

```bash
# ensure venv has pip and tools
.venv/bin/python -m ensurepip --upgrade
.venv/bin/python -m pip install --upgrade pip setuptools wheel

# install project packages in editable mode
.venv/bin/python -m pip install -e .
.venv/bin/python -m pip install -e packages/fastapi_feeder

# install uv CLI into the venv
.venv/bin/python -m pip install uv

# run apps with uv from the venv
.venv/bin/uv run llmv3
.venv/bin/uv run fastapi_feeder

# or run the quick smoke script
.venv/bin/python scripts/run_apps.py
```