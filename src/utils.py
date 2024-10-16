import json
import os

from dotenv import load_dotenv
from langchain import hub
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_openai import ChatOpenAI

# Clear the environment variables
# os.environ.clear()

# Load environment variables from the .env file
# dotenv_path = os.path.join(os.path.dirname(__file__), "../.env")
load_dotenv()


def setup_llm() -> object:
    """
    Initialize the large language model.

    Returns:
        object: A Large Language Model instance.
    """

    # load the json string from the env
    llm_settings_str= os.environ.get("MODEL_SETTINGS")

    # Parse the JSON string into a dictionary
    llm_settings = json.loads(llm_settings_str)

    # Create and configure the ChatOpenAI model instance
    llm_model = ChatOpenAI(
        model_name=llm_settings.get("model_name"),
        streaming=llm_settings.get("streaming"),
        callbacks=[StreamingStdOutCallbackHandler()],
        verbose=True
    )
    return llm_model

# Setting up llm Model
llm= setup_llm()

def get_memory(session_id) -> object:
    """
    Retrieve conversational memory for a given session ID.

    Args:
        session_id (str): The session ID for which memory is requested.

    Returns:
        object: Conversational Memory object.
    """
    # Create a RedisChatMessageHistory instance for storing message history
    message_history = RedisChatMessageHistory(
        url=os.environ.get("REDIS_URL"), ttl=600, session_id=session_id)
    return message_history

def get_prompt(prompt_id) -> str:
    """
    Fetch a prompt from the Langchain hub.

    Args:
        prompt_id (str): The ID of the prompt to fetch.

    Returns:
        str: The fetched prompt.
    """
    print("returning prompt")
    return hub.pull(prompt_id)


# if __name__ == "__main__":
#     print(get_prompt("alq-ai-team/wildfloc-chain"))