# KrishiMitra AI - System Architecture

## Overview

KrishiMitra AI is a microservice-based agricultural intelligence platform that helps farmers with:

* Crop recommendations
* Plant disease detection
* Weather alerts
* Market price intelligence
* AI-powered farming assistance

The system follows Domain Driven Design (DDD) principles and consists of independent FastAPI microservices communicating through REST APIs and asynchronous events.

---

## High-Level Architecture

```mermaid
flowchart TB

    User[Farmer Mobile/Web App]

    Gateway[API Gateway]

    Crop[Crop Recommendation Service]
    Disease[Disease Detection Service]
    Weather[Weather Alert Service]
    Market[Market Price Service]
    Agent[AI Agent Service]

    PostgreSQL[(PostgreSQL)]
    Redis[(Redis Cache)]

    MQ[Message Queue]

    User --> Gateway

    Gateway --> Crop
    Gateway --> Disease
    Gateway --> Weather
    Gateway --> Market
    Gateway --> Agent

    Crop --> PostgreSQL
    Disease --> PostgreSQL
    Weather --> PostgreSQL
    Market --> PostgreSQL
    Agent --> PostgreSQL

    Crop --> Redis
    Disease --> Redis
    Weather --> Redis
    Market --> Redis
    Agent --> Redis

    Crop <--> MQ
    Disease <--> MQ
    Weather <--> MQ
    Market <--> MQ
    Agent <--> MQ
```

---

## AI Agent Architecture

The AI Agent acts as an orchestration layer.

Business logic remains inside dedicated services.

```mermaid
flowchart LR

    UserQuery[Farmer Question]

    Router[LangGraph Router]

    CropTool[Crop Tool]
    DiseaseTool[Disease Tool]
    WeatherTool[Weather Tool]
    MarketTool[Market Tool]

    Response[Response Generator]

    UserQuery --> Router

    Router --> CropTool
    Router --> DiseaseTool
    Router --> WeatherTool
    Router --> MarketTool

    CropTool --> Response
    DiseaseTool --> Response
    WeatherTool --> Response
    MarketTool --> Response

    Response --> FinalAnswer[Farmer Response]
```

---

## Service Responsibilities

### API Gateway

Responsibilities:

* Authentication
* Request routing
* Rate limiting
* API aggregation
* Logging

---

### Crop Recommendation Service

Responsibilities:

* Crop recommendation
* Fertilizer recommendation
* Yield prediction
* Soil analysis

Technologies:

* FastAPI
* Scikit-learn
* PostgreSQL

---

### Disease Detection Service

Responsibilities:

* Image upload
* OpenCV preprocessing
* Disease classification
* Treatment recommendations

Technologies:

* FastAPI
* OpenCV
* TensorFlow/PyTorch

---

### Weather Alert Service

Responsibilities:

* Weather forecasts
* Weather alerts
* Crop risk assessments
* Notification generation

Technologies:

* FastAPI
* APScheduler

---

### Market Price Service

Responsibilities:

* Mandi prices
* Price trends
* Market comparisons
* Sell recommendations

Technologies:

* FastAPI
* Scheduled crawlers

---

### AI Agent Service

Responsibilities:

* Multi-tool reasoning
* Context management
* Conversation memory
* Service orchestration

Technologies:

* LangGraph
* LangChain
* Gemini/OpenAI

---

## Database Architecture

### Shared PostgreSQL

Initial MVP uses a shared PostgreSQL database.

Tables:

* users
* farms
* crops
* disease_reports
* weather_alerts
* market_prices
* conversations
* recommendations

Future scaling may split databases per service.

---

## Event-Driven Communication

Events:

* disease.detected
* weather.alert.generated
* crop.recommendation.generated
* market.price.updated

Example flow:

```mermaid
sequenceDiagram

    participant Disease
    participant MQ
    participant Agent

    Disease->>MQ: disease.detected
    MQ->>Agent: consume event
    Agent->>Agent: generate insights
```

---

## Deployment Architecture

```mermaid
flowchart TB

    Internet

    LB[Load Balancer]

    Frontend[Web App]

    Gateway[API Gateway]

    Crop[Crop Service]
    Disease[Disease Service]
    Weather[Weather Service]
    Market[Market Service]
    Agent[AI Agent]

    DB[(PostgreSQL)]
    Cache[(Redis)]

    Internet --> LB

    LB --> Frontend
    LB --> Gateway

    Gateway --> Crop
    Gateway --> Disease
    Gateway --> Weather
    Gateway --> Market
    Gateway --> Agent

    Crop --> DB
    Disease --> DB
    Weather --> DB
    Market --> DB
    Agent --> DB

    Crop --> Cache
    Disease --> Cache
    Weather --> Cache
    Market --> Cache
    Agent --> Cache
```

---

## Future Enhancements

* Kafka for event streaming
* Kubernetes deployment
* Vector database for AI memory
* RAG over agricultural knowledge base
* Multilingual voice assistant
* Real-time pest outbreak prediction
* Satellite imagery integration
