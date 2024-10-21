from utils import llm, get_prompt

class ChainManager:
    """
        Initializes the ChainManager.
    """

    def __init__(self):
        pass

    def create_chain(self, prompt_id: str):
        """
        Creates a chain by fetching a prompt based on the provided ID and appending it to the chain.

        Args:
            prompt_id (str): The ID of the prompt used to generate the chain.

        Returns:
            chain: A chain formed by combining the fetched prompt with the model.
        """

        # Fetch prompt based on the provided prompt ID
        prompt= get_prompt(prompt_id)
        print("______")
        print(prompt)

        # Concatenate the fetched prompt with the model
        return prompt | llm