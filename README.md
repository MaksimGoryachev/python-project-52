### Tests and linter status:
[![Actions Status](https://github.com/MaksimGoryachev/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/MaksimGoryachev/python-project-52/actions)

[//]: # ([![Actions Status]&#40;https://github.com/MaksimGoryachev/python-project-83/actions/workflows/check.yml/badge.svg&#41;]&#40;https://github.com/MaksimGoryachev/python-project-83/actions&#41;)

[//]: # ([![Maintainability]&#40;https://api.codeclimate.com/v1/badges/7f8ca67d141d78aedc6d/maintainability&#41;]&#40;https://codeclimate.com/github/MaksimGoryachev/python-project-83/maintainability&#41;)

---
## Description

[Task Manager](https://python-project-83-r9xq.onrender.com) is a website that analyzes specified pages for SEO suitability.

[demo GIF](images/demo_page_analyzer.gif)

---
## Instalation

You must have python 3.12 and newer, poetry and postgresql installed to work properly

### Repository cloning
Clone the repository to your computer `git clone https://github.com/MaksimGoryachev/python-project-83`

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