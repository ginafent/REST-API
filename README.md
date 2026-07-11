# REST API
Service feedback database and API

FastAPI's generated interactive docs are also available at `http://localhost:8000/docs`.


## Stack
1. PostgreSQL
1. Python and FastAPI
1. Docker Compose 

## Usage
Prerequisite: Docker is installed and running. (docker compose up --build)

## API
### GET /services/{service_id}
Returns the details for the service, which includes customer and feedback they gave. 

For example,
GET http://localhost:8000/services/1


#### Response
```json
{
  "serviceID": 1,
  "customer": {
    "customerID": 1,
    "firstName": "Alice",
    "lastName": "Smith"
  },
  "feedback": [
    { "feedbackID": 1, "comment": "Good service." }
  ]
}
```

If the service doesn't exist, returns `404`:
```json
{ "detail": "Service 1 not found" }
```

## Schema

- `customers` customerID, first/last name
- `services`  serviceID, linked to a customer
- `feedback` feedbackID, linked to a service, comment

Seed data (2 customers, 2 services, 2 feedback entries) is loaded automatically
from `db/init.sql` on first startup.