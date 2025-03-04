### Tests and linter status:
[![Actions Status](https://github.com/MaksimGoryachev/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MaksimGoryachev/python-project-52/actions)
[![Actions Status](https://github.com/MaksimGoryachev/python-project-52/actions/workflows/check.yml/badge.svg)](https://github.com/MaksimGoryachev/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/c7645ed894fc71e6244f/maintainability)](https://codeclimate.com/github/MaksimGoryachev/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c7645ed894fc71e6244f/test_coverage)](https://codeclimate.com/github/MaksimGoryachev/python-project-52/test_coverage)

---
### Description

[Task Manager](https://python-project-52-9hb2.onrender.com): is a web application built with Python and Django that allows users to manage tasks, statuses, and labels. It supports full CRUD (Create, Read, Update, Delete) operations for tasks, users, statuses, and labels. The application is designed to be simple, intuitive, and easy to use.

Key features:
- User registration and authentication.
- Task management with statuses and labels.
- Filtering tasks by status, performer, and label.
- Responsive design using Bootstrap 5.
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


### Installation with Docker

#### _Repository cloning_
First, clone the repository to your local machine:
```bash
>> git clone git@github.com:MaksimGoryachev/python-project-52.git && cd python-project-52
```

#### _Environment Variables_

To configure the application, you need to configure the necessary environment variables. A detailed example of these variables can be found in the .env.example file. Copy it to the .env file and replace the placeholders with your actual values:

    DATABASE_URL=postgres://<USER>:<PASSWORD>@<HOST>:<PORT>/<DATABASE>
    SECRET_KEY=<your-secret-key-here> # Django will refuse to start if SECRET_KEY is not set
    DEBUG=False
    POSTGRES_DB=<DATABASE>
    POSTGRES_USER=<USER>
    POSTGRES_PASSWORD=<PASSWORD>

#### _Run application with docker-compose_

To build and start the application using Docker, run:

```bash
>> docker-compose up --build
```
Once the containers are up and running, the application will be available at http://0.0.0.0:8000

### Installation without Docker

To run the application without Docker, ensure you have the following installed:
- Python 3.12 or newer
- PostgreSQL
- `uv` (a fast Python package manager)

#### _Repository cloning_

First, clone the repository to your local machine:
```bash
>> git clone git@github.com:MaksimGoryachev/python-project-52.git && cd python-project-52
```

#### _Environment Variables_

To configure the application, you need to configure the necessary environment variables. A detailed example of these variables can be found in the .env.example file. Copy it to the .env file and replace the placeholders with your actual values:

    DATABASE_URL=postgres://<USER>:<PASSWORD>@<HOST>:<PORT>/<DATABASE>
    SECRET_KEY=<your-secret-key-here> # Django will refuse to start if SECRET_KEY is not set
    DEBUG=False

#### _Database creation_

```shell
whoami
{username}
sudo -u postgres createuser --createdb {username} 
createdb {databasename}
```

#### _Installing package_

Install the package and apply the database migrations:
```shell
>> make setup
```

Create a superuser (optional)

Create a superuser to access the Django admin panel:
```shell
>> python manage.py createsuperuser
```
---

### Usage

#### _Start the Gunicorn Web-server by running:_

```shell
>> make start
```

By default, the server will be available at http://0.0.0.0:8000.

#### _Start the app on the local dev server_

```shell
>> make dev
```

The dev server will be at http://127.0.0.1:8000.

---

### Available Actions:

    Registration — First, you need to register in the application using the registration form provided;
    Authentication — To use the application, you need to log in using the information from the registration form.
    Users — You can see the list of all registered users on the corresponding page. It is available without authorization. User can change or delete information only about yourself;
    Statuses — You can view, add, update, and delete task statuses if you are logged in. Statuses used in existing tasks cannot be deleted;
    Tasks — You can view, add, and update tasks if you are logged in. Only the task creator can delete tasks. You can also filter tasks on the corresponding page with specified statuses, performers, and labels;
    Labels — You can view, add, update, and delete task labels if you are logged in. Labels used in existing tasks cannot be deleted.