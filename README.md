# Reading list

A small Flask app used as the test surface for an agentic dev pipeline. It keeps books in memory, exposes a JSON API, and renders a single HTML page.

## Run

```
pip install -r requirements.txt
python app.py
```

## Test

```
pytest
```

## API

| Method | Path | Purpose |
|---|---|---|
| GET | `/api/books` | List books |
| POST | `/api/books` | Add a book (`title` required, `author` optional) |
| POST | `/api/books/<id>/read` | Mark a book as read |
