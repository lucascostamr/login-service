FROM python:3.12-slim-bullseye
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN pip install poetry==2.1.2 \
    && poetry config virtualenvs.create false \
    && poetry install --no-root
HEALTHCHECK --interval=3s --timeout=10s --start-period=5s --retries=3 CMD [ "poetry" ]
ENV PYTHONPATH=/app/app
CMD ["poetry", "run", "python", "main.py"]