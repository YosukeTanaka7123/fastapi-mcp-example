from fastapi import FastAPI
from tinydb import TinyDB, Query
from tinydb.table import Document

from models.contact import Contact

app = FastAPI()

# TinyDB database initialization
db = TinyDB("db.json")


@app.get("/contacts", tags=["contacts"])
def get_contacts_all():
    contacts = db.table("contacts").all()
    return [Contact(**contact) for contact in contacts]


@app.post("/contacts", tags=["contacts"], status_code=201)
def post_contacts(payload: Contact):
    db.table("contacts").insert(payload.model_dump())
    return payload


@app.get("/contacts/{user_id}", tags=["contacts"])
def get_contacts_by_id(user_id: str):
    ContactsQuery = Query()
    contact = db.table("contacts").get(ContactsQuery.userId == user_id)
    if isinstance(contact, Document):
        return Contact(**contact)
    return None


@app.delete("/contacts/{user_id}", tags=["contacts"], status_code=204)
def delete_contacts(user_id: str):
    ContactsQuery = Query()
    db.table("contacts").remove(ContactsQuery.userId == user_id)
