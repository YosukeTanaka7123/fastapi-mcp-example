from pydantic import BaseModel
from typing import Optional


class Contact(BaseModel):
    """
    LINE user profile model.
    This model represents the profile information of a LINE user.
    """

    display_name: str
    user_id: str
    picture_url: Optional[str] = None
    status_message: Optional[str] = None
    language: Optional[str] = None
