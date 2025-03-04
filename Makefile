UV := uv run
UVPM:= uv run python manage.py
PORT ?= 8000

install:
	uv sync

dev:
	${UVPM} runserver

static:
	${UVPM} collectstatic --no-input

migrate:
	${UVPM} makemigrations
	${UVPM} migrate

start:
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

setup: build install migrate static

selfcheck:
	uv pip check

check: selfcheck lint

trans:
	${UV} django-admin makemessages --ignore="static" --ignore="index1.html" -l ru_RU
	${UV} django-admin compilemessages

test:
	${UV} python manage.py test task_manager

coverage:
	${UV} coverage run manage.py test task_manager
	${UV} coverage report -m --include=task_manager/* --omit=task_manager/settings.py
	${UV} coverage xml --include=task_manager/* --omit=task_manager/settings.py
	${UV} coverage html --include=task_manager/* --omit=task_manager/settings.py

.PHONY: install lint1 lint selfcheck check build start dev setup fix migrate shell static makemessages compilemessages trans test coverage