# TASKLY API

Just lke Trello, Taskly API the backend service of a collaboration tool that organizes your projects into boards. Taskly tells you what's being worked on, who's working on what, and where something is in a process. Imagine a white board, filled with lists of sticky notes, with each note as a task for you and your team - that is Taskly.

## Technologies 

The following technologies were used in this project:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.comg)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [MySQL](https://www.mysql.com)

## Requirements

Before starting, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/)installed. Alternatively, you can download the code as a zip file

## Clone this project

    git clone https://github.com/benidevo/taskly-api.git

## Create virtual environment

    python3 -m venv env

## Activate virtual environment

    . env/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate

## Start server

    python manage.py runserver
