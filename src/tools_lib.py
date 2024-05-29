import sys

# Adding paths to import custom modules
sys.path.insert(1, "src")
sys.path.insert(2, "app")
sys.path.insert(3, "config")

from langchain_core.tools import tool
from web_search_tool import WebSearchTool
from settings_manager import fetch_settings


@tool
def search_tool_wildfloc(question: str):
    """This is a websearch tool that you can use for question about any website url"""
    settings = fetch_settings("wildfloc")
    web_search = WebSearchTool(settings)
    response = web_search.ws_tool(question)
    return response


# Putting all tools together
tools_list_wildfloc = [search_tool_wildfloc]
@tool
def search_tool_cqai(question: str):
    """This is a websearch tool that you can use for question about any website url"""
    settings = fetch_settings("cqai")
    web_search = WebSearchTool(settings)
    response = web_search.ws_tool(question)
    return response
tools_list_cqai = [search_tool_wildfloc]