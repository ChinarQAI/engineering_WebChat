# WebChat Service - API Documentation

## Overview

The "app" directory within the WebChat service houses the API implementation logic using FastAPI. It contains the following files:

1. **router.py**: This file defines the FastAPI application and its endpoints for handling incoming HTTP requests. It includes endpoints for invoking the chatbot agent, updating settings, and fetching settings. The implementation leverages custom modules such as input schemas and settings manager functions to process requests and interact with external services.

2. **settingsmanager.py**: This file contains functions for managing application settings using Redis as a data store. It includes functions to insert new settings and fetch existing settings for a given application ID. Settings are stored as JSON strings in Redis, allowing for easy retrieval and modification.

3. **schemas.py**: This file defines Pydantic models for input validation and serialization. It includes models for representing query input and settings input, ensuring that incoming data adheres to specified schemas before processing.

## Files Description

### 1. router.py

- **Purpose:** Defines the FastAPI application and its endpoints for handling incoming HTTP requests.
- **Endpoints:**
  - `/invoke/{app_id}`: Invokes the chatbot agent function using the provided `app_id` and input parameters.
  - `/settings/{app_id}`:
    - `POST`: Updates the settings for a specific application identified by the `app_id`.
    - `GET`: Fetches the settings for a specific application identified by the `app_id`.
  - `/`: Root endpoint indicating the service is healthy and running.
- **Dependencies:** Uses custom input schemas and settings manager functions to process requests.
- **Execution:** Utilizes uvicorn to run the FastAPI application on a specified host and port.

### 2. settingsmanager.py

- **Purpose:** Contains functions for managing application settings using Redis as a data store.
- **Functions:**
  - `insert_settings(app_id, new_settings)`: Inserts new settings for the specified application ID into Redis.
  - `fetch_settings(app_id)`: Fetches existing settings for the specified application ID from Redis.
- **Dependencies:** Utilizes the Redis client library and reads environment variables from a .env file for Redis connection configuration.

### 3. schemas.py

- **Purpose:** Defines Pydantic models for input validation and serialization.
- **Models:**
  - `QueryInput`: Represents the input for a query, including session ID, query text, and username.
  - `SettingsInput`: Represents the input for settings, including a dictionary containing settings information.

## How It Works

The FastAPI application in `router.py` serves as the backend API for the WebChat service. When a client sends a request to one of the defined endpoints, the corresponding function is executed to process the request. Input data is validated using Pydantic models defined in `schemas.py`, ensuring that it conforms to specified schemas before further processing. Application settings are managed using functions defined in `settingsmanager.py`, which interact with a Redis instance to store and retrieve settings data.

By following RESTful principles, the API endpoints enable clients to interact with the WebChat service, invoke the chatbot agent, and manage application settings effectively.

