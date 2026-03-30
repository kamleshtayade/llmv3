from fastapi import FastAPI, Request

# Import the router that contains endpoint handlers.
from .routes import router

app = FastAPI()


@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    """A tiny example middleware that adds a header to every response.

    This keeps the feeder as a middleware-capable FastAPI app.
    """
    response = await call_next(request)
    response.headers["X-FastAPI-Feeder"] = "1"
    return response


# Include application routes from the `routes` module. Keeping a flat
# `main.py` that only wires the app makes the code follow single-responsibility
# principles and eases testing.
app.include_router(router)


def main():
    # Simple CLI entrypoint for manual testing if desired
    print("This module exposes a FastAPI `app` instance.")


def serve(host: str = "127.0.0.1", port: int = 8000, reload: bool = False):
    """Run the ASGI app with uvicorn.

    Kept as a separate function so importing this module doesn't start a
    server (important for TestClient-based consumers and unit tests).
    """
    # Import uvicorn lazily to avoid requiring it on simple imports
    try:
        import uvicorn
    except Exception as e:
        raise RuntimeError("uvicorn is required to serve the app") from e

    uvicorn.run("fastapi_feeder.main:app", host=host, port=port, reload=reload)


if __name__ == "__main__":
    # When executed directly, start the server for manual testing
    serve()
 