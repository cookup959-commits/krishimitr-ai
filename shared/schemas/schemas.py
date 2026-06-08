from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    phone: Optional[str] = None
    user_id: Optional[int] = None

# User & Profile Schemas
class UserCreate(BaseModel):
    name: str
    phone: str
    password: str
    location: Optional[str] = None
    farm_size: Optional[float] = None

class UserLogin(BaseModel):
    phone: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    phone: str
    location: Optional[str]
    farm_size: Optional[float]
    created_at: datetime

    class Config:
        from_attributes = True

class ProfileUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    farm_size: Optional[float] = None

# Crop Recommendation Schemas
class CropRecommendRequest(BaseModel):
    soil_type: Optional[str] = "Black"
    nitrogen: float = Field(..., ge=0, le=200)
    phosphorus: float = Field(..., ge=0, le=200)
    potassium: float = Field(..., ge=0, le=200)
    temperature: float = Field(..., ge=-10, le=60)
    humidity: float = Field(..., ge=0, le=100)

class CropRecommendResponse(BaseModel):
    recommended_crop: str
    confidence: float
    reason: Optional[str] = None

class FertilizerRequest(BaseModel):
    crop_name: str
    soil_type: str
    nitrogen_level: float
    phosphorus_level: float
    potassium_level: float

class FertilizerResponse(BaseModel):
    fertilizer: str
    quantity: str
    reason: Optional[str] = None

class YieldRequest(BaseModel):
    crop_name: str
    farm_size: float
    soil_type: str
    expected_rainfall: Optional[float] = 100.0

class YieldResponse(BaseModel):
    estimated_yield: str
    unit: str = "quintals"

# Disease Detection Schemas
class DiseaseDetectResponse(BaseModel):
    disease: str
    confidence: float
    severity: str
    treatment: List[str]

class TreatmentResponse(BaseModel):
    disease: str
    treatment: List[str]

# Weather Schemas
class WeatherCurrentResponse(BaseModel):
    temperature: float
    humidity: float
    condition: str
    wind_speed: float

class WeatherForecastDay(BaseModel):
    day: str
    temp: float
    condition: str

class WeatherForecastResponse(BaseModel):
    days: List[WeatherForecastDay]

class WeatherAlertItem(BaseModel):
    type: str
    severity: str
    description: str

class WeatherAlertResponse(BaseModel):
    alerts: List[WeatherAlertItem]

# Market Schemas
class MarketItem(BaseModel):
    name: str
    price: float

class MarketPriceResponse(BaseModel):
    commodity: str
    markets: List[MarketItem]

class MarketComparisonResponse(BaseModel):
    best_market: str
    best_price: float
    commodity: str

class PriceTrendResponse(BaseModel):
    trend: str
    change_percent: float
    commodity: str

# AI Agent Schemas
class AgentChatRequest(BaseModel):
    session_id: str
    message: str

class AgentChatResponse(BaseModel):
    response: str

class ChatMessageOut(BaseModel):
    role: str
    message: str
    created_at: datetime

    class Config:
        from_attributes = True

class ChatHistoryResponse(BaseModel):
    messages: List[ChatMessageOut]
