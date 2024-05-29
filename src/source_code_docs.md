# WebChat Service - Source Code Documentation

## Overview

The "srs" directory within the WebChat service contains the source code files responsible for managing and executing the chatbot agents and custom chains. It includes the following files:

1. **ast_main.py**: This file defines the AgentManager class responsible for initializing and configuring the chatbot agent for execution. It also contains the execute_agent function, which executes the agent using the provided input parameters and settings.

2. **custom_chain.py**: This file contains the ChainManager class responsible for creating custom chains by fetching prompts based on provided IDs. It also defines the create_chain method to create a chain by combining fetched prompts with the model.

3. **tools_lib.py**: This file contains custom tools used by the chatbot agent for performing specific tasks. It defines functions such as search_tool_wildfloc for web search and provides a list of tools used by the agent.

4. **utils.py**: This file contains utility functions used by the chatbot agent and custom chains. It includes functions such as setup_llm for initializing the language model and get_memory for retrieving conversational memory.

5. **web_search_tool.py**: This file contains the WebSearchTool class responsible for performing web searches using the configured search API. It includes methods for performing searches, extracting URLs from search results, and cleaning text.

## Files Description

### 1. ast_main.py

- **Purpose:** Initializes and configures the chatbot agent for execution and defines the execute_agent function for agent execution.
- **Dependencies:** Uses utility functions from utils.py and imports the AgentExecutor class from langchain.agents.

### 2. custom_chain.py

- **Purpose:** Creates custom chains by fetching prompts based on provided IDs and concatenating them with the model.
- **Dependencies:** Uses utility functions from utils.py and imports the ChainManager class from langchain.

### 3. tools_lib.py

- **Purpose:** Defines custom tools used by the chatbot agent for performing specific tasks, such as web search.
- **Dependencies:** Imports modules for web search and settings management.

### 4. utils.py

- **Purpose:** Contains utility functions used by the chatbot agent and custom chains, such as initializing the language model and retrieving conversational memory.
- **Dependencies:** Imports modules for language model setup and conversational memory management.

### 5. web_search_tool.py

- **Purpose:** Performs web searches using the configured search API and provides methods for search execution, URL extraction, and text cleaning.
- **Dependencies:** Imports modules for web search utilities and settings management.

## How It Works

The source code files in the "srs" directory work together to manage and execute the chatbot agents and custom chains. 

- **ast_main.py** initializes and configures the chatbot agent for execution and defines the execute_agent function to execute the agent using provided input parameters and settings.
- **custom_chain.py** creates custom chains by fetching prompts based on provided IDs and concatenating them with the model.
- **tools_lib.py** defines custom tools used by the chatbot agent for performing specific tasks, such as web search.
- **utils.py** contains utility functions used by the chatbot agent and custom chains, such as initializing the language model and retrieving conversational memory.
- **web_search_tool.py** performs web searches using the configured search API and provides methods for search execution, URL extraction, and text cleaning.

Together, these files enable the chatbot service to effectively manage and execute agents and custom chains, providing users with accurate and relevant responses to their queries.

