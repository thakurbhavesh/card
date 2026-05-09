#!/usr/bin/env bash
# Render build script
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input

# During build, Render's internal Postgres DNS doesn't resolve.
# Force settings.py to keep the external hostname for migrate.
export RENDER_BUILD_PHASE=1

# External SSL handshake is flaky on cold connect; retry up to 5x.
for attempt in 1 2 3 4 5; do
    if python manage.py migrate --no-input; then
        echo "migrate succeeded on attempt $attempt"
        break
    fi
    if [ "$attempt" -eq 5 ]; then
        echo "migrate failed after 5 attempts"
        exit 1
    fi
    echo "migrate attempt $attempt failed, retrying in $((attempt * 5))s..."
    sleep $((attempt * 5))
done
