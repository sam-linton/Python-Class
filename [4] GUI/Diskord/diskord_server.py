from typing import Union

from fastapi import FastAPI

app = FastAPI()

# In-memory storage
messages = []


@app.get("/")
def get_messages():
    """Return the list of all messages."""
    return messages


@app.get("/message/{message}")
def add_message(message: str):
    """Add a new message to the list."""
    print(message)
    messages.append(message)
    return {"status": "ok", "added": message}
