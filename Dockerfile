# Etap 1
FROM python:3.12 AS builder

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

# Etap 2
FROM builder AS test

RUN pip install pytest

RUN pytest

# Etap 3
FROM python:3.12-slim AS final

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 5000

CMD ["python", "run.py"]
