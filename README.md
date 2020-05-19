# Panzofi basic auth

This is a test for an interview with Panzofi, the purpose of this repo, is to create a Django server to handle two types of users (normal and administrator), and a button counter per user; also, to create a React portal that consumes the Django server.

## How to run it

1. Clone this repository

1. Be sure you have installed `docker` and `docker-compose` on your machine.
    
    If you dont have `docker-compose` installed, follow this guide to install it on your OS.
    https://docs.docker.com/compose/install/

1. Run
    ```bash
    docker-compose up -d --build
    docker-compose exec backend python basic_auth/manage.py migrate --settings=basic_auth.settings.development --noinput
    docker-compose exec backend python basic_auth/manage.py create_admin_user --settings=basic_auth.settings.development
    docker-compose exec backend python basic_auth/manage.py create_random_users --settings=basic_auth.settings.development
    ```
   
    - It will run a database in postgres, then it will start the Django server, at last it will mount a nginx server to deploy the portal
    - Run the migrations
    - Setup the initial data

## Information

### Admin credentials

```
username: admin
password: qwerty
```

### Users credentials

35 users will be created, their respective credentials would be

```
username: user_{n}
password: qwerty_{n}
```

`n` between [0, 34]

for example, the user 12

```
username: user_12
password: qwerty_12
```

### Portal

You can open the portal on your web browser typing
http://localhost

### Database

You can access to the database using your favorite database manager with following credentials

```
DATABASE_HOST=127.0.0.1
DATABASE_NAME=basic-auth
DATABASE_PASSWORD=backend
DATABASE_PORT=5432
DATABASE_USER=backend
```
