# URL Shortener App (Demo)

![](https://img.shields.io/badge/python-3.10-blue)
![](https://img.shields.io/badge/FastAPI-0.78-red)
![](https://img.shields.io/badge/SQLAlchemy-1.4-green)

Demo app for creating and managing short versions of the user-provide URL's. Based on [RealPython tutorial](https://realpython.com/build-a-python-url-shortener-with-fastapi/).

### This app uses Poetry ([Install Poetry](https://python-poetry.org/docs/master/#installation))

## Installing dependancies

```bash
poetry install
```

## Setting environmental variables

Rename `.env-sample >> .env` and provide the values listed in it.

## Running the app

```bash
uvicorn shortener_app.main:app --reload
```

## Accessing API documentation

> [**localhost:8000/docs**](localhost:8000/docs)
