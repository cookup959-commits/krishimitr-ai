# KrishiMitra AI API Specifications

Base URL

```text
/api/v1
```

---

# Authentication

## Login

```http
POST /auth/login
```

Request

```json
{
  "phone": "9876543210",
  "password": "password"
}
```

Response

```json
{
  "access_token": "jwt",
  "refresh_token": "jwt"
}
```

---

## Register

```http
POST /auth/register
```

Request

```json
{
  "name": "Ramesh",
  "phone": "9876543210",
  "location": "Nashik"
}
```

---

# Crop Recommendation Service

## Get Crop Recommendation

```http
POST /crop/recommend
```

Request

```json
{
  "farm_id": 1,
  "soil_type": "Black",
  "nitrogen": 45,
  "phosphorus": 25,
  "potassium": 35,
  "temperature": 28,
  "humidity": 70
}
```

Response

```json
{
  "recommended_crop": "Cotton",
  "confidence": 0.92
}
```

---

## Fertilizer Recommendation

```http
POST /crop/fertilizer
```

Response

```json
{
  "fertilizer": "Urea",
  "quantity": "50kg/acre"
}
```

---

## Yield Prediction

```http
POST /crop/yield
```

Response

```json
{
  "estimated_yield": "120 quintals"
}
```

---

# Disease Detection Service

## Detect Disease

```http
POST /disease/detect
```

Multipart Form

```text
image=file
```

Response

```json
{
  "disease": "Tomato Leaf Curl Virus",
  "confidence": 0.95,
  "severity": "Moderate"
}
```

---

## Treatment Recommendation

```http
GET /disease/treatment/{disease_name}
```

Response

```json
{
  "disease": "Tomato Leaf Curl Virus",
  "treatment": [
    "Remove infected leaves",
    "Apply neem oil"
  ]
}
```

---

# Weather Alert Service

## Current Weather

```http
GET /weather/current
```

Response

```json
{
  "temperature": 28,
  "humidity": 65,
  "condition": "Sunny"
}
```

---

## Forecast

```http
GET /weather/forecast
```

Response

```json
{
  "days": [
    {
      "day": "Monday",
      "temp": 29
    }
  ]
}
```

---

## Weather Alerts

```http
GET /weather/alerts
```

Response

```json
{
  "alerts": [
    {
      "type": "Heavy Rain",
      "severity": "High"
    }
  ]
}
```

---

# Market Price Service

## Commodity Prices

```http
GET /market/prices?commodity=tomato&latitude=19.9975&longitude=73.7898&radius_km=50
```

Query Parameters:
* `commodity` (required): Name of the crop/commodity.
* `latitude` (optional): User's current latitude. If omitted, falls back to the user's registered profile location.
* `longitude` (optional): User's current longitude. If omitted, falls back to the user's registered profile location.
* `radius_km` (optional, default 50): Search radius for finding closest mandis.

Response

```json
{
  "commodity": "Tomato",
  "user_coords": {
    "latitude": 19.9975,
    "longitude": 73.7898
  },
  "markets": [
    {
      "name": "Pimpalgaon Mandi",
      "price": 4150,
      "distance_km": 12.4,
      "state": "Maharashtra",
      "district": "Nashik"
    },
    {
      "name": "Nashik Main Mandi",
      "price": 4200,
      "distance_km": 15.1,
      "state": "Maharashtra",
      "district": "Nashik"
    }
  ]
}
```

---

## Market Comparison

```http
GET /market/comparison?commodity=tomato&latitude=19.9975&longitude=73.7898
```

Response

```json
{
  "commodity": "Tomato",
  "best_market": {
    "name": "Nashik Main Mandi",
    "price": 4200,
    "distance_km": 15.1
  },
  "alternative_markets": [
    {
      "name": "Pimpalgaon Mandi",
      "price": 4150,
      "distance_km": 12.4
    }
  ]
}
```

---

## Price Trend

```http
GET /market/trends?commodity=tomato
```

Response

```json
{
  "trend": "upward",
  "change_percent": 12.5
}
```

---

# AI Agent Service

## Chat

```http
POST /agent/chat
```

Request

```json
{
  "session_id": "abc123",
  "message": "Should I sell my tomatoes this week?"
}
```

Response

```json
{
  "response": "Tomato prices are rising and weather conditions are favorable. Selling this week is recommended."
}
```

---

## Conversation History

```http
GET /agent/history/{session_id}
```

Response

```json
{
  "messages": []
}
```

---

# Profile Service

## Get Profile

```http
GET /profile
```

Response

```json
{
  "name": "Ramesh",
  "location": "Nashik",
  "farm_size": 12.5
}
```

---

## Update Profile

```http
PUT /profile
```

---

# Health Checks

Each service must expose:

```http
GET /health
```

Response

```json
{
  "status": "healthy"
}
```

---

# Internal Service Endpoints

These endpoints are used only by the AI Agent.

```http
POST /internal/crop/recommend

POST /internal/disease/detect

GET /internal/weather/current

GET /internal/weather/forecast

GET /internal/market/prices
```

These endpoints should be protected by service-to-service authentication.
