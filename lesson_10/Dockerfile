# Stage 1 -> load dependencies

FROM python:3.11-slim-bullseye as base_image

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

ENV POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir poetry==1.5.1

RUN poetry install --no-root && \
    rm -rf $POETRY_CACHE_DIR

# Stage 2 -> copy dependencies from stage 1, start application

FROM python:3.11-slim-bullseye

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY --from=base_image ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY ./ ./

# CMD ["ls", "-la", "."]
ENTRYPOINT ["granian", "--interface", "asgi", "--host", "0.0.0.0", "--port", "8000", "lesson_10"]
