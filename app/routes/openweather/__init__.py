from fastapi import APIRouter, HTTPException

from app.clients.openweather import OpenWeatherApiClientDep
from app.routes.openweather.schema import WeatherResponse, GeocodingResponse

router = APIRouter(tags=["openweather"])


@router.get("/openweather/current", response_model=WeatherResponse)
def get_current_weather(
    city: str, open_weather_api_client: OpenWeatherApiClientDep
):
    geocoding_response = open_weather_api_client.get_geocoding(city)

    if not geocoding_response:
        raise HTTPException(
            status_code=404,
            detail=f"City '{city}' not found",
        )

    geocoding_response_model = GeocodingResponse.model_validate(
        geocoding_response[0]
    )
    return open_weather_api_client.get_current_weather(
        lat=geocoding_response_model.lat, lon=geocoding_response_model.lon
    )
