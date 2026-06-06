# KrishiMitra AI

AI-powered agricultural intelligence platform built using FastAPI microservices, LangGraph agents, OpenCV disease detection, weather intelligence, and market analytics.

---

## Features

### Farmer Features

* Crop Recommendation
* Fertilizer Recommendation
* Yield Prediction
* Disease Detection from Images
* Treatment Suggestions
* Weather Forecasts
* Weather Alerts
* Mandi Price Tracking
* Market Comparison
* AI Farming Assistant
* Voice-based Queries
* Multilingual Support
* Government Scheme Tracking

---

## Tech Stack

### Frontend

* React
* TypeScript
* Vite
* Tailwind CSS
* Konsta UI

### Backend

* FastAPI
* Python 3.12

### AI

* LangChain
* LangGraph
* Gemini / OpenAI

### Computer Vision

* OpenCV
* PyTorch / TensorFlow

### Database

* PostgreSQL

### Cache

* Redis

### Infrastructure

* Docker
* Kubernetes (Future)
* Nginx

---

# System Architecture

```text
Web App
    │
    ▼
API Gateway
    │
    ├── Crop Recommendation Service
    ├── Disease Detection Service
    ├── Weather Alert Service
    ├── Market Price Service
    └── AI Agent Service
             │
             ▼
         LangGraph
             │
             ▼
     Service Orchestration

Shared Resources
    ├── PostgreSQL
    ├── Redis
    └── Message Queue
```

---

# Repository Structure

```text
krishimitra/
│
├── README.md
├── .gitignore
├── docker-compose.yml
├── .env
│
├── web-app/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── services/
│   │   ├── context/
│   │   ├── routes/
│   │   ├── store/
│   │   ├── utils/
│   │   └── App.tsx
│   │
│   ├── package.json
│   └── Dockerfile
│
├── services/
│   │
│   ├── api-gateway/
│   │
│   ├── crop-recommendation-service/
│   │
│   ├── disease-detection-service/
│   │
│   ├── weather-alert-service/
│   │
│   ├── market-price-service/
│   │
│   └── ai-agent-service/
│
├── shared/
│   ├── auth/
│   ├── cache/
│   ├── database/
│   ├── schemas/
│   ├── events/
│   └── utils/
│
├── infrastructure/
│   ├── docker/
│   ├── kubernetes/
│   └── monitoring/
│
├── data/
│
└── docs/
    ├── architecture.md
    ├── api-specs.md
    └── database-design.md
```

---

# Service Overview

## API Gateway

Responsibilities:

* Authentication
* Authorization
* Rate Limiting
* Request Routing
* Logging

Port:

```text
8000
```

---

## Crop Recommendation Service

Responsibilities:

* Crop Recommendation
* Fertilizer Recommendation
* Yield Prediction
* Soil Analysis

Port:

```text
8001
```

---

## Disease Detection Service

Responsibilities:

* Image Processing
* Disease Classification
* Treatment Suggestions

Port:

```text
8002
```

---

## Weather Alert Service

Responsibilities:

* Weather Forecasting
* Weather Alerts
* Crop Risk Analysis

Port:

```text
8003
```

---

## Market Price Service

Responsibilities:

* Mandi Price Tracking
* Market Comparison
* Price Trend Analysis

Port:

```text
8004
```

---

## AI Agent Service

Responsibilities:

* Farmer Chat Interface
* Multi-tool Reasoning
* Context Management
* Service Orchestration

Port:

```text
8005
```

---

# Local Development

## Clone Repository

```bash
git clone https://github.com/your-org/krishimitra.git

cd krishimitra
```

---

## Start Infrastructure

```bash
docker-compose up -d postgres redis
```

---

## Run Services

### Crop Service

```bash
cd services/crop-recommendation-service

uvicorn app.main:app --reload --port 8001
```

### Disease Service

```bash
cd services/disease-detection-service

uvicorn app.main:app --reload --port 8002
```

### Weather Service

```bash
cd services/weather-alert-service

uvicorn app.main:app --reload --port 8003
```

### Market Service

```bash
cd services/market-price-service

uvicorn app.main:app --reload --port 8004
```

### AI Agent Service

```bash
cd services/ai-agent-service

uvicorn app.main:app --reload --port 8005
```

### API Gateway

```bash
cd services/api-gateway

uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd web-app

npm install

npm run dev
```

---

# Environment Variables

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/krishimitra

REDIS_URL=redis://localhost:6379

GEMINI_API_KEY=your_key

OPENAI_API_KEY=your_key

JWT_SECRET=secret
```

---

# AI Agent Design

The AI Agent is an orchestrator.

It should never contain business logic.

Example:

Farmer asks:

> Should I sell my tomatoes this week?

Agent Flow:

```text
User Query
    │
    ▼
LangGraph Router
    │
    ├── Market Tool
    ├── Weather Tool
    └── Crop Tool
    │
    ▼
Response Generator
    │
    ▼
Final Recommendation
```

This ensures all business rules remain inside dedicated services.

---

# Documentation

* docs/architecture.md
* docs/api-specs.md
* docs/database-design.md

---

# Future Roadmap

## Phase 1

* Authentication
* Crop Recommendation
* Disease Detection
* Weather Alerts
* Market Prices
* AI Chat Assistant

## Phase 2

* Voice Assistant
* Multilingual AI
* Push Notifications
* Government Schemes

## Phase 3

* Satellite Imagery Analysis
* Pest Outbreak Prediction
* Farm Analytics Dashboard
* Predictive Market Intelligence

---

# Contributors

Backend Team

* FastAPI Services
* LangGraph Agent
* PostgreSQL
* Redis

Frontend Team

* React
* Vite
* Konsta UI

AI Team

* LangChain
* LangGraph
* OpenCV
* ML Models
