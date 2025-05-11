from fastapi import APIRouter, Response
from tinydb import Query
from tinydb.table import Document
from typing import List

from app.dependencies import SessionDep
from app.routes.contacts.schema import Contact

router = APIRouter(tags=["contacts"])


@router.get("/contacts", response_model=List[Contact])
def get_contacts_all(session: SessionDep):
    contacts = session.table("contacts").all()
    return [Contact(**contact) for contact in contacts]


@router.post("/contacts", response_model=Contact, status_code=201)
def post_contacts(payload: Contact, session: SessionDep):
    session.table("contacts").insert(payload.model_dump())
    return payload


@router.get(
    "/contacts/{user_id}",
    response_model=Contact,
    responses={204: {"description": "No Content"}},
)
def get_contacts_by_id(user_id: str, session: SessionDep):
    ContactsQuery = Query()
    contact = session.table("contacts").get(ContactsQuery.user_id == user_id)
    if isinstance(contact, Document):
        return Contact(**contact)
    return Response(status_code=204, content=None)


@router.delete("/contacts/{user_id}", status_code=204)
def delete_contacts(user_id: str, session: SessionDep):
    ContactsQuery = Query()
    session.table("contacts").remove(ContactsQuery.user_id == user_id)
