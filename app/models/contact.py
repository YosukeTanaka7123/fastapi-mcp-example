from pydantic import BaseModel
from typing import Optional


class Contact(BaseModel):
    """
    LINE user profile model.
    This model represents the profile information of a LINE user.
    """

    displayName: str
    userId: str
    language: Optional[str] = None
    pictureUrl: Optional[str] = None
    statusMessage: Optional[str] = None
