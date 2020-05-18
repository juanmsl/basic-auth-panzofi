FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    default-libmysqlclient-dev \
    libssl-dev \
    libffi-dev \
    libcurl4-openssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code && chown user:user /code

COPY requirements/ /code/requirements

RUN pip install -r /code/requirements/development.txt

RUN pip install -r /code/requirements/production.txt

ADD . /code

WORKDIR /code

USER user

EXPOSE 8585

CMD ["uwsgi", "--ini", "basic_auth/basic_auth/uwsgi.ini"]
