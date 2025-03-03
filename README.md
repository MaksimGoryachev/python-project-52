### Tests and linter status:
[![Actions Status](https://github.com/MaksimGoryachev/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MaksimGoryachev/python-project-52/actions)
[![Actions Status](https://github.com/MaksimGoryachev/python-project-52/actions/workflows/check.yml/badge.svg)](https://github.com/MaksimGoryachev/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/c7645ed894fc71e6244f/maintainability)](https://codeclimate.com/github/MaksimGoryachev/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c7645ed894fc71e6244f/test_coverage)](https://codeclimate.com/github/MaksimGoryachev/python-project-52/test_coverage)

---
### Description

[Task Manager](https://python-project-52-9hb2.onrender.com): this is a web application that allows you to implement the full lifecycle (CRUD) of users and their tasks. The application is built with Python and Django framework.


---
### Links

This project was built using these tools:

| Tool                                                      | Description                                             |
|-----------------------------------------------------------|---------------------------------------------------------|
| [Django](https://www.djangoproject.com/)                  | "A high-level Python web framework that encourages rapid development and clean, pragmatic design." |
| [Bootstrap 5](https://getbootstrap.com/)                  | "A popular CSS framework for building responsive and mobile-first web projects."            |
| [PostgreSQL](https://www.postgresql.org/)                 | "A powerful, open-source relational database management system." |
| [Gunicorn](https://gunicorn.org/)                         | "A WSGI server for Unix, used to deploy Python applications." |
| [Docker](https://www.docker.com/)                         | "A platform for developing, shipping, and running applications in containers."            |
| [uv](https://docs.astral.sh/uv/)                          | "An extremely fast Python package and project manager, written in Rust" |
| [dj-database-url](https://pypi.org/project/dj-database-url/)| "A Django utility that allows you to configure databases using URL-style strings." |
| [Whitenoise](http://whitenoise.evans.io/en/latest/)       | "A library for serving static files in Python applications." |
| [Rollbar](https://rollbar.com/)                           | "A tool for error monitoring and real-time issue tracking." |
| [ruff](https://docs.astral.sh/ruff/)                      | "An extremely fast Python linter and code formatter, written in Rust" |
| [Flake8](https://flake8.pycqa.org/en/latest/)             | "A tool for checking Python code style and quality."            |
| [Coverage.py](https://coverage.readthedocs.io/en/7.6.12/) | "A tool for measuring code coverage of Python programs." |

## Installation

### _Installation with Docker_

You must have python 3.12 and newer, uv and postgresql installed to work properly

#### Repository cloning
Clone the repository to your computer:
```bash
>> git clone git@github.com:MaksimGoryachev/python-project-52.git && cd python-project-52
```

#### Environment Variables

To configure the application, you need to set up the required environment variables. A detailed example of these variables can be found in the .env.example file. Create an `.env` file in the root of the project and add the following variables to it:

    DATABASE_URL=postgres://<USER>:<PASSWORD>@<HOST>:<PORT>/<DATABASE>
    SECRET_KEY=<your-secret-key-here> # Django will refuse to start if SECRET_KEY is not set
    DEBUG=False
    POSTGRES_DB=<DATABASE>
    POSTGRES_USER=<USER>
    POSTGRES_PASSWORD=<PASSWORD>

For a complete example, refer to the .env.example file. Copy it to .env and replace the placeholders with your actual values.

#### Run application 

Docker will create the image and the necessary containers with a single command:
```bash
>> docker-compose up --build
```
The server is running at http://0.0.0.0:8000
### Database creation
```sh
whoami
{username}
sudo -u postgres createuser --createdb {username} 
createdb {databasename}
```

### Installing dependencies
Install the package `make setup`

---

## Start the app on the local dev server
`make dev`

---
## Start the app on the production server
`make start`

---
