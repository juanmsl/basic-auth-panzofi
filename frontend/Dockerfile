FROM node:8-slim

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    build-essential \
    default-libmysqlclient-dev \
    libssl-dev \
    libffi-dev \
    libcurl4-openssl-dev \
    && rm -rf /var/lib/apt/lists/* \
    && curl -o- -L https://yarnpkg.com/install.sh | bash

RUN mkdir -p /code && chown user:user /code

RUN mkdir -p /usr/share/nginx/html && chown user:user /usr/share/nginx/html

COPY package.json yarn.lock /code/

RUN yarn

ADD . /code

WORKDIR /code

RUN npm rebuild node-sass

RUN yarn build

COPY /code/build/* /usr/share/nginx/html/

USER user