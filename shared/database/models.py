import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from shared.database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    location = Column(String, nullable=True)
    farm_size = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    disease_reports = relationship("DiseaseReport", back_populates="user")
    conversations = relationship("Conversation", back_populates="user")

class Crop(Base):
    __tablename__ = "crops"

    id            = Column(Integer, primary_key=True, index=True)
    name          = Column(String, nullable=False, unique=True)
    nitrogen      = Column(Float, nullable=False)
    phosphorus    = Column(Float, nullable=False)
    potassium     = Column(Float, nullable=False)
    temp_min      = Column(Float, nullable=False)
    temp_max      = Column(Float, nullable=False)
    humidity_min  = Column(Float, nullable=False)
    humidity_max  = Column(Float, nullable=False)
    description   = Column(Text, nullable=True)

class DiseaseReport(Base):
    __tablename__ = "disease_reports"

    id           = Column(Integer, primary_key=True, index=True)
    user_id      = Column(Integer, ForeignKey("users.id"), nullable=False)
    image_path   = Column(String, nullable=False)
    disease_name = Column(String, nullable=False)
    confidence   = Column(Float, nullable=False)
    severity     = Column(String, nullable=False)  # Low, Moderate, High
    treatment    = Column(Text, nullable=True)
    created_at   = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="disease_reports")

class WeatherAlert(Base):
    __tablename__ = "weather_alerts"

    id = Column(Integer, primary_key=True, index=True)
    alert_type = Column(String, nullable=False)  # Heavy Rain, Drought, Frost, Heatwave
    severity = Column(String, nullable=False)   # Low, Moderate, High
    description = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class MarketPrice(Base):
    __tablename__ = "market_prices"

    id = Column(Integer, primary_key=True, index=True)
    commodity = Column(String, nullable=False, index=True)
    market_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.datetime.utcnow)

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    role = Column(String, nullable=False)  # user, assistant
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = relationship("User", back_populates="conversations")

class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    soil_type = Column(String, nullable=True)
    nitrogen = Column(Float, nullable=True)
    phosphorus = Column(Float, nullable=True)
    potassium = Column(Float, nullable=True)
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    recommended_crop = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
