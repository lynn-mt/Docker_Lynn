FROM python:3.13.11-slim    
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

COPY pyproject.toml .python-version uv.lock ./
##run pip install pandas pyarrow  
WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"
COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked


COPY pipeline.py .
entrypoint ["python", "pipeline.py"]
