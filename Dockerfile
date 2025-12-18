# Etap 1
FROM python:3.12 AS builder

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

# Etap 2
FROM builder AS test

ENV PYTHONPATH=/app

RUN pip install pytest

RUN pytest

# Etap 3
FROM python:3.12-slim AS final

WORKDIR /app

ENV PYTHONPATH=/app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

COPY docker/seed_script.sh /seed_script.sh
RUN chmod +x /seed_script.sh

EXPOSE 5000

CMD ["python", "run.py"]
