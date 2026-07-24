# Flask Contacts API

A minimal Flask REST API demonstrating JSON endpoints over an in-memory list of contacts.

## Endpoints
- `GET /get-data` — returns all contacts as JSON.
- `POST /add-data` — appends a contact. Body: `{ "Contact": "555-0104", "Name": "Erin" }`.
  Returns a 400-style error if no JSON body is provided.

## Run

```bash
pip install flask
python app2.py        # serves on http://127.0.0.1:5000 in debug mode
```

## Example

```bash
curl http://127.0.0.1:5000/get-data
curl -X POST http://127.0.0.1:5000/add-data \
  -H "Content-Type: application/json" \
  -d '{"Contact":"555-0104","Name":"Erin"}'
```

> Note: the seed data uses placeholder names/numbers. An earlier version committed real personal
> phone numbers; those have been removed from the code and from git history.
