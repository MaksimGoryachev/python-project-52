#!/usr/bin/env bash
# Exit on error
set -o errexit

# скачиваем uv и запускаем команду установки зависимостей
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
# Modify this line as needed for your package manager (pip, poetry, etc.)
uv pip install .

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate