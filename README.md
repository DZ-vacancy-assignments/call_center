kpn call center
===============

Minimalistic version of KPN standard call center experience.

<a href="https://github.com/vchaptsev/cookiecutter-django-vue">
    <img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg" />
</a>


## Development

Install [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/). Start your virtual machines with the following shell command:

`docker-compose up --build`

If all works well, you should be able to create an admin account with:

`docker-compose run backend python manage.py createsuperuser`

For certain Django logging functionality you need to create the file:

`./logs/django.log`

## For development the following settings should suffice in the root .env file:

```python
DEBUG=True
SECRET_KEY=<secret-key>

DOMAIN=http://localhost:8000
ALLOWED_HOSTS=localhost

DJANGO_SUPERUSER_PASSWORD=<password>
DJANGO_SUPERUSER_EMAIL=admin@kpncallcenter.com

# PostgreSQL
# Will have to be created manually.
POSTGRES_DB=kpn_callcenter
POSTGRES_PASSWORD=<password>
POSTGRES_USER=postgresuser

# Google Analytics
VUE_APP_GOOGLE_ANALYTICS=UA-XXXXXXXXX-X
```
