from  pydantic import BaseModel
class QueryInput(BaseModel):
    """
    Represents the input for a query.

    Attributes:
        session_id (str): The unique identifier for the session.
        query (str): The text of the query.
    """
    session_id: str  # Unique identifier for the session
    query: str  # Text of the query
    username: str

class SettingsInput(BaseModel):
    """
    Represents the input for settings.

    Attributes:
        settings (dict): A dictionary containing settings information.
    """
    settings: dict  # Dictionary containing settings information
