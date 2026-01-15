from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PredictionRequest(BaseModel):
    energy: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Perceptual measure of intensity and activity (0.0-1.0)"
    )
    valence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Musical positivity/happiness (0.0-1.0)"
    )
    tempo: float = Field(
        ...,
        gt=0,
        description="Overall estimated tempo in BPM (typically 50-200)"
    )
    acousticness: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Confidence the track is acoustic (0.0-1.0)"
    )
    loudness: float = Field(
        ...,
        description="Overall loudness in decibels (typically -60 to 0)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "energy": 0.8,
                "valence": 0.9,
                "tempo": 120.0,
                "acousticness": 0.2,
                "loudness": -5.0
            }
        }


class PredictionResponse(BaseModel):
    weather: str = Field(
        ...,
        description="Predicted weather category: sunny, cloudy, rainy, or snowy"
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Prediction confidence score"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "weather": "sunny",
                "confidence": 0.85
            }
        }


class SongSearchRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=1,
        description="Song search query (e.g., 'Happy - Pharrell Williams')"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "query": "Happy - Pharrell Williams"
            }
        }


class SongWeatherResponse(BaseModel):
    track_id: str
    name: str
    artist: str
    album: str
    image_url: Optional[str]
    preview_url: Optional[str]
    weather: str = Field(description="Predicted weather: sunny, cloudy, rainy, or snowy")
    confidence: float = Field(ge=0.0, le=1.0, description="Prediction confidence")
    audio_features: Dict[str, float]

    class Config:
        json_schema_extra = {
            "example": {
                "track_id": "60nZcImufyMA1MKQY3dcCH",
                "name": "Happy",
                "artist": "Pharrell Williams",
                "album": "G I R L",
                "image_url": "https://i.scdn.co/image/...",
                "preview_url": "https://p.scdn.co/mp3-preview/...",
                "weather": "sunny",
                "confidence": 0.92,
                "audio_features": {
                    "energy": 0.8,
                    "valence": 0.9,
                    "tempo": 160.0,
                    "acousticness": 0.1,
                    "loudness": -5.0
                }
            }
        }


class HealthResponse(BaseModel):
    status: str
    message: str
    model_loaded: bool
    model_info: Optional[Dict[str, Any]] = None
