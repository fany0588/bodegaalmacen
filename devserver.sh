#!/bin/bash

source .venv/bin/activate

# Use the PORT environment variable provided by the preview environment, or default to 8081.
LISTEN_PORT=${PORT:-8081}

echo "Starting server on port $LISTEN_PORT"

python backend_BodegaAlmacen/manage.py runserver 0.0.0.0:$LISTEN_PORT --noreload
