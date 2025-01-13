import os 
import sys
# Adding paths to import custom modules
sys.path.insert(1, "src")
sys.path.insert(2, "app")
sys.path.insert(3, "config")
import re

from langchain_community.utilities import GoogleSerperAPIWrapper

# Importing custum chain
from custom_chain import ChainManager
from settings_manager import fetch_settings

# Fetching API keys from environment variables
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class SearchTool:
    def __init__(self, settings: dict):
        """
        Initializes the SearchTool with the provided settings.

        Args:
            settings (dict): Dictionary containing settings for the SearchTool.
        """
        self.settings = settings
        self.search_api = GoogleSerperAPIWrapper(serper_api_key=SERPER_API_KEY)

    def perform_search(self, query: str):
        """
        Performs a search using the configured search API.

        Args:
            query (str): The search query.

        Returns:
            tuple: A tuple containing the search response and a list of extracted URLs.
        """
        print(self.settings['Tools']['wb_tool']['website_url'], type(self.settings))
        # Accessing the website_url
        website_url = self.settings['Tools']['wb_tool']['website_url']
        print("++++++WEBSITE URL+++++++++")
        print(website_url)
        modified_query = f"site:{website_url} {query}"
        response = self.search_api.run(query=modified_query)
        results = self.search_api.results(modified_query)
        return response, self._extract_urls(results)
    
    @staticmethod
    def _extract_urls(results: dict):
        """
        Extracts URLs from search results.

        Args:
            results (dict): The search results.

        Returns:
            list: A list of extracted URLs.
        """
        url_list = set(result['link'] for result in results.get('organic', []))
        return list(url_list)

    @staticmethod
    def clean_text(text: str):
        """
        Cleans the text by removing Markdown links and extra whitespaces.

        Args:
            text (str): The text to clean.

        Returns:
            str: The cleaned text.
        """
        text_without_md_links = re.sub(r"\[.*?\]\(.*?\)", "", text)
        cleaned_text = re.sub(r"\s+", " ", text_without_md_links).strip()
        return cleaned_text

class WebSearchTool:
    def __init__(self, settings: dict):
        """
        Initializes the WebSearchTool with the provided settings.

        Args:
            settings (dict): Dictionary containing settings for the WebSearchTool.
        """
        self.settings= settings
        self.search_tool= SearchTool(settings)
        self.chain_manager= ChainManager()
    
    def ws_tool(self, query: str):
        """
        Executes the web search tool.

        Args:
            query (str): The search query.

        Returns:
            object: Results of the web search.
        """

        search_response, sources= self.search_tool.perform_search(query)
        print("+++++++++++++++++++++++++++Search Response++++++++++++++++++++++++")
        print(search_response)
        search_response= self.search_tool.clean_text(search_response)
        print(f'CHAIN PROMPT ID{self.settings["Tools"]["wb_tool"]["prompt_id"]}')
        chain= self.chain_manager.create_chain(prompt_id=self.settings["Tools"]["wb_tool"]["prompt_id"])
        results= chain.invoke({"question": query, "context": (search_response, sources)})
        return results

