from fastapi import APIRouter

from linebot.v3.messaging import PushMessageRequest as LinePushMessageRequest

from app.dependencies import LineApiClientDep
from app.models.contact import Contact
from app.routes.linebot.schema import (
    PushMessageRequest,
    PushMessageResponse,
    MessageQuotaResponse,
)

router = APIRouter(tags=["linebot"])


@router.get("/linebot/profile/{user_id}", response_model=Contact)
def get_profile(user_id: str, line_api_client: LineApiClientDep):
    response = line_api_client.get_profile(user_id)
    return Contact(**response.dict())


@router.post(
    "/linebot/push-text-message",
    response_model=PushMessageResponse,
)
def post_push_text_message(
    payload: PushMessageRequest, line_api_client: LineApiClientDep
):
    response = line_api_client.push_message(
        push_message_request=LinePushMessageRequest.from_dict(
            payload.model_dump()
        )
    )
    return PushMessageResponse(**response.dict())


@router.get("/linebot/message-quota", response_model=MessageQuotaResponse)
def get_message_quota(line_api_client: LineApiClientDep):
    quota_response = line_api_client.get_message_quota()
    quota_consumption_response = (
        line_api_client.get_message_quota_consumption()
    )

    return MessageQuotaResponse(
        limited=quota_response.value or 0,
        total_usage=quota_consumption_response.total_usage,
    )
