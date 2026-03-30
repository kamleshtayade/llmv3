from fastapi import FastAPI, Request

app = FastAPI()


@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    """A tiny example middleware that adds a header to every response.

    This keeps the feeder as a middleware-capable FastAPI app.
    """
    response = await call_next(request)
    response.headers["X-FastAPI-Feeder"] = "1"
    return response


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

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
 