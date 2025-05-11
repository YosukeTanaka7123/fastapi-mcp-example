from typing import Annotated, Optional, List
from pydantic import (
    BaseModel,
    Field,
    StrictStr,
    conlist,
    StrictInt,
    StrictFloat,
)


class LocalNames(BaseModel):
    ja: Optional[StrictStr] = Field(..., description="Local name in Japanese")


class GeocodingResponse(BaseModel):
    name: StrictStr = Field(..., description="Name of the found location")
    local_names: LocalNames = Field(
        ...,
        description="Local names of the city in different languages",  # noqa: E501
    )
    lat: StrictFloat = Field(
        ...,
        description="Geographical coordinates of the found location (latitude)",  # noqa: E501
    )
    lon: StrictFloat = Field(
        ...,
        description="Geographical coordinates of the found location (longitude)",  # noqa: E501
    )
    country: StrictStr = Field(
        ..., description="Country of the found location"
    )
    state: Optional[StrictStr] = Field(
        None, description="State of the found location"
    )


class Coord(BaseModel):
    lon: StrictFloat = Field(..., description="Longitude of the location")
    lat: StrictFloat = Field(..., description="Latitude of the location")


class Weather(BaseModel):
    id: StrictInt = Field(..., description="Weather condition id")
    main: StrictStr = Field(
        ...,
        description="Group of weather parameters (Rain, Snow, Clouds etc.)",
    )
    description: StrictStr = Field(
        ..., description="Weather condition within the group"
    )
    icon: StrictStr = Field(..., description="Weather icon id")


class Main(BaseModel):
    temp: StrictFloat = Field(
        ...,
        description="Temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit",  # noqa: E501
    )
    feels_like: StrictFloat = Field(
        ...,
        description="This temperature parameter accounts for the human perception of weather. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit",  # noqa: E501
    )
    pressure: StrictInt = Field(
        ..., description="Atmospheric pressure on the sea level, hPa"
    )
    humidity: StrictInt = Field(..., description="Humidity, %")
    temp_min: StrictFloat = Field(
        ...,
        description="Minimum temperature at the moment. This is minimal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit",  # noqa: E501
    )
    temp_max: StrictFloat = Field(
        ...,
        description="Maximum temperature at the moment. This is maximal currently observed temperature (within large megalopolises and urban areas). Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit",  # noqa: E501
    )
    sea_level: Optional[StrictInt] = Field(
        None, description="Atmospheric pressure on the sea level, hPa"
    )
    grnd_level: Optional[StrictInt] = Field(
        None, description="Atmospheric pressure on the ground level, hPa"
    )


class Wind(BaseModel):
    speed: StrictFloat = Field(
        ...,
        description="Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour",  # noqa: E501
    )
    deg: StrictInt = Field(
        ..., description="Wind direction, degrees (meteorological)"
    )
    gust: Optional[StrictFloat] = Field(
        None,
        description="Wind gust. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour",  # noqa: E501
    )


class Clouds(BaseModel):
    all: StrictInt = Field(..., description="Cloudiness, %")


class Rain(BaseModel):
    one_hour: Optional[StrictFloat] = Field(
        None,
        alias="1h",
        description="Rain volume for the last hour in mm. Unit Default: mm, Metric: mm, Imperial: mm",  # noqa: E501
    )


class Snow(BaseModel):
    one_hour: Optional[StrictFloat] = Field(
        None,
        alias="1h",
        description="Snow volume for the last hour in mm. Unit Default: mm, Metric: mm, Imperial: mm",  # noqa: E501
    )


class Sys(BaseModel):
    type: Optional[StrictInt] = Field(None, description="Internal parameter")
    id: Optional[StrictInt] = Field(None, description="Internal parameter")
    country: StrictStr = Field(..., description="Country code (GB, JP etc.)")
    sunrise: StrictInt = Field(..., description="Sunrise time, unix, UTC")
    sunset: StrictInt = Field(..., description="Sunset time, unix, UTC")


class WeatherResponse(BaseModel):
    coord: Coord = Field(..., description="Coordinates of the location")
    weather: Annotated[List[Weather], conlist(Weather, min_length=1)] = Field(
        ..., description="Weather conditions"
    )
    base: StrictStr = Field(..., description="Internal parameter")
    main: Main = Field(..., description="Main weather parameters")
    visibility: StrictInt = Field(..., description="Visibility in meters")
    wind: Wind = Field(..., description="Wind information")
    clouds: Clouds = Field(..., description="Cloud information")
    rain: Optional[Rain] = Field(
        None,
        description="Rain information",
    )
    snow: Optional[Snow] = Field(
        None,
        description="Snow information",
    )
    dt: StrictInt = Field(
        ..., description="Time of data calculation, unix, UTC"
    )
    sys: Sys = Field(..., description="System information")
    timezone: StrictInt = Field(..., description="Shift in seconds from UTC")
    id: StrictInt = Field(..., description="City ID")
    name: StrictStr = Field(..., description="City name")
    cod: StrictInt = Field(..., description="Internal parameter")
