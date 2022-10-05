FROM python:3.9


ARG BASIC_AUTH_USERNAME_ARG
ARG BASIC_AUTH_PASSWORD_ARG

ENV BASIC_AUTH_USERNAME=$BASIC_AUTH_USERNAME_ARG
ENV BASIC_AUTH_PASSWORD=$BASIC_AUTH_PASSWORD_ARG

COPY ./requirements.txt /usr/requirements.txt

WORKDIR /usr

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src /usr/src
COPY ./models /usr/models

# ENTRYPOINT [ "python3" ]

CMD [ "gunicorn --chdir src/app/ main:app" ]


