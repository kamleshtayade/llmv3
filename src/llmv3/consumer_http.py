"""HTTP consumer that calls the feeder endpoints over the network.

This is intended to run inside the consumer container and call the feeder container
by its service name (docker-compose network). When running under Docker Compose
the feeder service may take a few seconds to become ready; this module will
retry a few times with backoff so a first-time `docker compose up --build` is
more likely to succeed without manual intervention.
"""
import os
import sys
import time
import requests

# Default to the docker-compose service hostname so the container works with
# the provided `docker-compose.yml`. Override with FEEDER_URL for local runs.
FEEDER_URL = os.environ.get("FEEDER_URL", "http://feeder:8000")

# Retry configuration (overridable via env)
MAX_RETRIES = int(os.environ.get("FEEDER_MAX_RETRIES", "12"))
RETRY_INTERVAL = float(os.environ.get("FEEDER_RETRY_INTERVAL", "1"))


def wait_for_feeder() -> bool:
    """Try to contact the feeder root endpoint with retries and exponential backoff.

    Returns True if the feeder responded with a successful HTTP status code,
    otherwise False after exhausting retries.
    """
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            r = requests.get(f"{FEEDER_URL}/", timeout=5)
            r.raise_for_status()
            print(f"Feeder reachable (attempt {attempt}) -> {r.status_code}")
            return True
        except Exception as exc:
            print(f"Feeder not ready (attempt {attempt}): {exc}", file=sys.stderr)
            if attempt >= MAX_RETRIES:
                return False
            # Exponential backoff (1, 2, 4, ... seconds scaled by RETRY_INTERVAL)
            sleep_time = RETRY_INTERVAL * (2 ** (attempt - 1))
            time.sleep(sleep_time)


def run():
    if not wait_for_feeder():
        print(
            f"Feeder at {FEEDER_URL} not reachable after {MAX_RETRIES} attempts, exiting",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        r = requests.get(f"{FEEDER_URL}/")
        print("GET / ->", r.status_code, r.json())
    except Exception as exc:
        print("GET / failed:", exc, file=sys.stderr)

    try:
        r2 = requests.get(f"{FEEDER_URL}/users")
        print("GET /users ->", r2.status_code, r2.json())
    except Exception as exc:
        print("GET /users failed:", exc, file=sys.stderr)


if __name__ == "__main__":
    run()
