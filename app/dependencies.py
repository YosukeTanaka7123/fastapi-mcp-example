from functools import lru_cache
from typing import Annotated

from fastapi import Depends
from tinydb import TinyDB
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from app.config import Settings


@lru_cache
def get_settings():
    return Settings()


SettingsDep = Annotated[Settings, Depends(get_settings)]


def get_db():
    # TinyDB database initialization
    with TinyDB("db.json") as session:
        yield session


SessionDep = Annotated[TinyDB, Depends(get_db)]


def get_line_api_client(settings: SettingsDep):
    # Configuration for the LINE Messaging API
    configuration = Configuration(access_token=settings.line_access_token)

    # Create an instance of the API class
    with ApiClient(configuration) as api_client:
        try:
            yield MessagingApi(api_client)
        except Exception as e:
            print("Exception when creating MessagingApi: %s\n" % e)


LineApiClientDep = Annotated[MessagingApi, Depends(get_line_api_client)]
