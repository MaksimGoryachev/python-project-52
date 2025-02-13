UV := uv run
UVPM:= uv run python manage.py

install:
	uv sync

dev:
	${UVPM} runserver

static:
	${UVPM} collectstatic --no-input

migrate:
	${UVPM} makemigrations
	${UVPM} migrate

PORT ?= 8000
start:
	${UV} gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

render-start:
	python -m gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi:application

build:
	./build.sh

lint1:
	${UV} flake8 task_manager

ruff:
	${UV} ruff check task_manager

fix:
	${UV} ruff check --fix task_manager

shell:
	${UVPM} shell

lint: lint1 ruff

setup: build install

selfcheck:
	uv pip check

check: selfcheck lint

trans:
	${UV} django-admin makemessages --ignore="static" --ignore="index1.html" -l ru_RU
	${UV} django-admin compilemessages


.PHONY: install lint1 lint selfcheck check build start render-start dev setup fix migrate shell static makemessages compilemessages trans