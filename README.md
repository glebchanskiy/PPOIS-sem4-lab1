# ATM model - LR1

## Install

Clone repository:

```sh
git clone https://github.com/glebchanskiy/....
```

Install python deps:

```sh
cd lab1
poetry install
```

## Run

Start db:

```sh
cd lab1/postgres-db
docker-compose up
```

Run app:

```sh
cd lab1
poetry run atm-client
```

---

## Dependencies

- poetry
- docker
