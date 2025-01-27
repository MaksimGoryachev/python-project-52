### Tests and linter status:
[![Actions Status](https://github.com/MaksimGoryachev/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MaksimGoryachev/python-project-52/actions)
[![Actions Status](https://github.com/MaksimGoryachev/python-project-52/actions/workflows/check.yml/badge.svg)](https://github.com/MaksimGoryachev/python-project-52/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/c7645ed894fc71e6244f/maintainability)](https://codeclimate.com/github/MaksimGoryachev/python-project-52/maintainability)

---
## Description

[Task Manager](https://python-project-52-9hb2.onrender.com): this is a web application that allows you to implement the full lifecycle (CRUD) of users and their tasks.

[//]: # ([demo GIF]&#40;images/demo_page_analyzer.gif&#41;)

---
## Instalation

You must have python 3.12 and newer, uv and postgresql installed to work properly

### Repository cloning
Clone the repository to your computer `git clone https://python-project-52-9hb2.onrender.com`

### Database creation
```sh
whoami
{username}
sudo -u postgres createuser --createdb {username} 
createdb {databasename}
```
### Secret keys
Two environment variables are required for the site to work: SECRET_KEY and DATABASE_URL. To define and store them, you can create a .env file in the project:

.env
```sh
DATABASE_URL='postgresql://{username}:{password}@{host}:{port}/{databasename}'
SECRET_KEY='{your secret key}'
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