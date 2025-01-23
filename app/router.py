import sys
import uvicorn
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect

# Adding paths to import custom modules
sys.path.insert(1, "src")
sys.path.insert(2, "app")
sys.path.insert(3, "config")
# Importing the websocket module
from ws_server import manager
# Importing input schemas
from schemas import QueryInput, SettingsInput

# Importing functions to fetch and update settings
from settings_manager import fetch_settings, insert_settings

# Importing the main function to execute the agent
from src.ast_main import execute_agent_0, execute_agent

# Creating a FastAPI instance
app = FastAPI()

# Root route
@app.get("/")
async def root():
    """
    Root endpoint of the FastAPI application.
    
    Returns:
        dict: A dictionary containing a message indicating that the service is healthy and running.
    """
    return {"message": "Service is healthy and running."}

@app.post("/invoke/{app_id}")
async def invoke_agent(app_id: str, query_input:QueryInput) -> dict:
    """
        Endpoint to invoke the agent driver function using the app_id and input parameters.

        Args:
            app_id (str): The name of the application.
            query_input (QueryInput): Input parameters including session_id and query.

        Returns:
            dict: Result returned by the agent.
        """
    in_params= {"app_id": app_id, "session_id": query_input.session_id, "query": query_input.query, "username": query_input.username}
    try:
        print("triyng to pront setting \n")
        settings= fetch_settings(app_id)
        print(settings)
        if settings is None:
            raise HTTPException(status_code=404, detail="Settings not found")
        result= execute_agent_0(in_params, settings)
        return {"result": result}
    except Exception as e:
        print("Loged here")
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/settings/{app_id}")
async def update_settings(app_id: str, settings_input: SettingsInput) -> dict:
    try:
        insert_settings(app_id, settings_input.settings)
        return {"message": "settings inserted sucessfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/settings/{app_id}")
async def get_settings(app_id: str) -> dict:
    try:
        settings= fetch_settings(app_id)
        return settings
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.websocket("/ws/invoke/{app_id}")
async def websocket_endpoint(websocket: WebSocket, app_id: str):
    """
    WebSocket endpoint to invoke the agent driver function using the app_id and input parameters.

    Args:
        websocket (WebSocket): The WebSocket connection.
        app_id (str): The name of the application.
    """
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            query_input = QueryInput(**data)
            in_params = {"app_name": app_id, "session_id": query_input.session_id, "query": query_input.query}
            try:
                settings = fetch_settings(app_id)
                if settings is None:
                    await manager.send_personal_message("Settings not found", websocket)
                    continue
                
                # Use async for to handle streaming response
                async for result in execute_agent(in_params, settings):
                    await manager.send_personal_message(result, websocket)
            except Exception as e:
                await manager.send_personal_message(f"Error: {str(e)}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)


if __name__ == "__main__":

    uvicorn.run(app=app, host="localhost", port= 8001)