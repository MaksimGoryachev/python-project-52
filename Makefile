install:
	uv sync

dev:
	uv run python manage.py runserver

static:
	uv run python manage.py collectstatic --no-input

migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate

PORT ?= 8000
start:
	uv run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

build:
	./build.sh

lint1:
	uv run flake8 task_manager

ruff:
	uv run ruff check task_manager

fix:
	uv run ruff check --fix task_manager

shell:
	uv run python manage.py shell

lint: lint1 ruff

setup: install build

selfcheck:
	uv check

check: selfcheck lint

.PHONY: install lint1 lint selfcheck check build start dev setup fix migrate shell static