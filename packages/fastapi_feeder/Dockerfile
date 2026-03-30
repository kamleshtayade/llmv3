# Feeder image: minimal Python runtime with FastAPI and uvicorn
FROM python:3.11-slim

WORKDIR /app

# Copy package source (src layout) so the module path is importable
COPY src/ ./src/

# Install only runtime dependencies. Avoid build tools since there are no C extensions.
RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates \
    && rm -rf /var/lib/apt/lists/* || true

# Pin runtime packages. uvicorn with standard extras for better performance.
RUN pip install --no-cache-dir "fastapi[standard]==0.113.0" "pydantic==2.8.0" "uvicorn[standard]==0.24.0"

# Ensure Python can import the package from /app/src
ENV PYTHONPATH=/app/src

EXPOSE 8000

# Run uvicorn directly; host 0.0.0.0 to be reachable from other containers
CMD ["uvicorn", "fastapi_feeder.main:app", "--host", "0.0.0.0", "--port", "8000"]
