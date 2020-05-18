# Panzofi basic auth

This is a test for an interview with Panzofi, the purpose of this repo, is to create a Django server to handle two types of users (normal and administrator), and a button counter per user; also, to create a React portal that consumes the Django server.

## How to run it

1. Clone this repository

1. Be sure you have installed `docker-compose` on your machine

1. Run
    ```bash
    docker-compose-up
    ```
   
    It will run a database in postgres, then it will start the Django server, an will run the migrations and setup the initial data, at last it will mount a nginx server to deploy the portal

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