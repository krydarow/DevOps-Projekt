#!/bin/sh
set -e

echo "Waiting for database..."

until python - << END
import os
import psycopg2
import sys

try:
    psycopg2.connect(dsn=os.environ["DATABASE_URL"])
except Exception:
    sys.exit(1)
END
do
  sleep 2
done

echo "Database is ready"
echo "Running seed script..."

python seed/run_seed.py

echo "Seeding finished"
