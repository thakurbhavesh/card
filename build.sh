#!/usr/bin/env bash
# Render build script — install deps + collect static only.
# Migrations run at startup (see startCommand in render.yaml) because
# Render's free Postgres external SSL endpoint refuses connections
# from the build container; the internal hostname only resolves at
# runtime.
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
