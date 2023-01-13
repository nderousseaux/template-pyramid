# Projet {{ cookiecutter.project_name_display }}

## Project setup

### Developpement
- Copy `.env.example` to `.env` and fill it with your parameters
- Run `docker-compose up` to start the containers or just press f5 if you are using vscode for debug.

### Production
- Copy `.env.example` to `.env` and fill it with your parameters
- Do `pip freeze > requirements.txt` to generate the requirements file.
- Run `docker-compose -f docker-compose.yml -f config/docker/docker-compose.prod.yml up`.
