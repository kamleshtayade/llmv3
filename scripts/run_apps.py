"""Quick smoke script to run both package main() functions.

Run: .venv/bin/python scripts/run_apps.py
"""

from importlib import import_module

apps = [
    ("llmv3", "llmv3.main"),
    ("fastapi_feeder", "fastapi_feeder.main"),
]

for name, module in apps:
    try:
        mod = import_module(module)
        print(f"Running {name} -> {module}.main()")
        if hasattr(mod, "main"):
            mod.main()
        else:
            print(f"{module} has no main() function")
    except Exception as e:
        print(f"Failed to run {name}: {e}")
