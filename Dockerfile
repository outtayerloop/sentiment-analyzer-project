#Retrieve 3.9 python version
FROM python:3.9

#Create code directory in docker container
WORKDIR /code

#Define environment variables
ARG APP_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0
ENV SENTIMENT_ANALYSIS_HOST=localhost
ENV FLASK_RUN_PORT=$APP_PORT

#Copy all project files and directories in docker container
COPY ./routes /code/routes
COPY ./services /code/services
COPY ./static /code/static
COPY ./templates /code/templates
COPY ./app.py /code/app.py
COPY ./poetry.lock /code/poetry.lock
COPY ./pyproject.toml /code/pyproject.toml
COPY ./README.md /code/README.md
COPY ./.env /code/.env

#Download poetry package manager
RUN pip install poetry

#Install project dependencies
RUN poetry install

#Define application running port
EXPOSE $APP_PORT

#Lauch app after container be instantiated
CMD ["poetry","run", "flask" , "run"]