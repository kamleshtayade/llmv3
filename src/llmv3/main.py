from fastapi.testclient import TestClient
import importlib.util
import sys
from pathlib import Path


# Load the feeder module by file path to make this consumer robust to
# different import/installation layouts.
def _load_feeder_module():
    repo_root = Path(__file__).resolve().parents[2]
    feeder_file = repo_root / "packages" / "fastapi_feeder" / "src" / "fastapi_feeder" / "main.py"
    spec = importlib.util.spec_from_file_location("fastapi_feeder.main", str(feeder_file))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def main():
    """Consumer that calls the feeder's '/' endpoint via TestClient.

    This keeps everything local and avoids starting a real server. It's a
    minimal demonstration of consuming the feeder API programmatically.
    """
    feeder_mod = _load_feeder_module()
    client = TestClient(feeder_mod.app)
    resp = client.get("/")
    print("status_code:", resp.status_code)
    print("json:", resp.json())
    print("feeder-header:", resp.headers.get("X-FastAPI-Feeder"))


if __name__ == "__main__":
    main()
