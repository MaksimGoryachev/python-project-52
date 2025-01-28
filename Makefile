MANAGE := uv run

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
	${MANAGE} gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

build:
	./build.sh

lint1:
	${MANAGE} flake8 task_manager

ruff:
	${MANAGE} ruff check task_manager

fix:
	${MANAGE} ruff check --fix task_manager

shell:
	${MANAGE} python manage.py shell

lint: lint1 ruff

setup: build install

selfcheck:
	uv pip check

check: selfcheck lint

trans:
	${MANAGE} django-admin makemessages --ignore="static" --ignore="index1.html" -l ru_RU
	${MANAGE} django-admin compilemessages


.PHONY: install lint1 lint selfcheck check build start dev setup fix migrate shell static makemessages compilemessages trans