"""Helper script to run the feeder app with uvicorn.

This provides a small convenience entrypoint for manual testing:

python scripts/run_feeder.py

It calls the serve() function exported by the feeder module.
"""
from fastapi_feeder.main import serve

if __name__ == "__main__":
    serve()
