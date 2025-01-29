UV := uv run

install:
	uv sync

dev:
	${UV} python manage.py runserver

static:
	${UV} python manage.py collectstatic --no-input

migrate:
	${UV} python manage.py makemigrations
	${UV} python manage.py migrate

PORT ?= 8000
start:
	${UV} gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

render-start:
	gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

build:
	./build.sh

lint1:
	${UV} flake8 task_manager

ruff:
	${UV} ruff check task_manager

fix:
	${UV} ruff check --fix task_manager

shell:
	${UV} python manage.py shell

lint: lint1 ruff

setup: build install

selfcheck:
	uv pip check

check: selfcheck lint

trans:
	${UV} django-admin makemessages --ignore="static" --ignore="index1.html" -l ru_RU
	${UV} django-admin compilemessages


.PHONY: install lint1 lint selfcheck check build start render-start dev setup fix migrate shell static makemessages compilemessages trans