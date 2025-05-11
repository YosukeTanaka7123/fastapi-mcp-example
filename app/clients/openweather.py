from typing import Annotated, Dict, List

from fastapi import Depends

from app.dependencies import SettingsDep


from httpx import Client, Timeout


class OpenWeatherApiClient:
    def __init__(self, api_key: str):
        self.base_url = "https://api.openweathermap.org"
        self.httpx_client = Client(
            timeout=Timeout(5.0, read=30.0), params={"appid": api_key}
        )

    def get_current_weather(self, lat: float, lon: float) -> Dict:
        path = "/data/2.5/weather"
        response = self.httpx_client.get(
            f"{self.base_url}{path}",
            params={"lat": lat, "lon": lon, "lang": "ja"},
        )
        return response.json()

    def get_geocoding(self, city: str) -> List[Dict]:
        path = "/geo/1.0/direct"
        response = self.httpx_client.get(
            f"{self.base_url}{path}",
            params={"q": city, "limit": 1},
        )
        return response.json()


def get_open_weather_api_client(settings: SettingsDep):
    return OpenWeatherApiClient(settings.open_weather_api_key)


OpenWeatherApiClientDep = Annotated[
    OpenWeatherApiClient, Depends(get_open_weather_api_client)
]
