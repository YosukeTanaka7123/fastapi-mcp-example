from typing import Annotated, Optional, List, Literal
from pydantic import BaseModel, Field, StrictStr, conlist, StrictBool


class UserProfileResponse(BaseModel):
    """
    UserProfileResponse
    https://developers.line.biz/en/reference/messaging-api/#get-profile
    """

    display_name: StrictStr = Field(..., description="User's display name")
    user_id: StrictStr = Field(..., description="User ID")
    picture_url: Optional[StrictStr] = Field(
        None,
        description="Profile image URL. `https` image URL. Not included in the response if the user doesn't have a profile image.",  # noqa: E501
    )
    status_message: Optional[StrictStr] = Field(
        None,
        description="User's status message. Not included in the response if the user doesn't have a status message.",  # noqa: E501
    )
    language: Optional[StrictStr] = Field(
        None,
        description="User's language, as a BCP 47 language tag. Not included in the response if the user hasn't yet consented to the LINE Privacy Policy.",  # noqa: E501
    )


class TextMessage(BaseModel):
    type: Literal["text"] = Field(
        "text", description="Type of the message. The value is always text."
    )
    text: StrictStr = Field(
        ...,
        max_length=5000,
        description="Text of the message.",
    )


class PushMessageRequest(BaseModel):
    """
    PushMessageRequest
    https://developers.line.biz/en/reference/messaging-api/#send-push-message
    """

    to: StrictStr = Field(..., description="ID of the receiver.")
    messages: Annotated[
        List[TextMessage], conlist(TextMessage, min_length=1, max_length=5)
    ] = Field(..., description="List of Message objects.")
    notification_disabled: Optional[StrictBool] = Field(
        False,
        description="`true`: The user doesn’t receive a push notification when a message is sent. `false`: The user receives a push notification when the message is sent (unless they have disabled push notifications in LINE and/or their device). The default value is false.",  # noqa: E501
    )
    custom_aggregation_units: Optional[List[StrictStr]] = Field(
        None,
        description="List of aggregation unit name. Case-sensitive. This functions can only be used by corporate users who have submitted the required applications.",  # noqa: E501
    )


class SentMessage(BaseModel):
    """
    SentMessage
    """

    id: StrictStr = Field(..., description="ID of the sent message.")
    quote_token: Optional[StrictStr] = Field(
        None,
        description="Quote token of the message. Only included when a message object that can be specified as a quote target was sent as a push or reply message. ",  # noqa: E501
    )


class PushMessageResponse(BaseModel):
    """
    PushMessageResponse
    https://developers.line.biz/en/reference/messaging-api/#send-push-message-response
    """

    sent_messages: Annotated[
        List[SentMessage], conlist(SentMessage, min_length=1, max_length=5)
    ] = Field(
        ...,
        description="Array of sent messages.",
    )


class MessageQuotaResponse(BaseModel):
    limited: int
    total_usage: int
