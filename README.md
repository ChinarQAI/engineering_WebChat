# WebChat

## Description

**Title: WebChat AI**

**Description:**

WebChat AI is a groundbreaking chatbot application that harnesses the power of artificial intelligence to facilitate seamless interactions between users and online content. With WebChat AI, users can engage in natural language conversations and access a wealth of information from across the web in real-time.

**Key Features:**

1. **Google Serper Integration:** WebChat AI leverages the Google Serper API to perform comprehensive web searches and retrieve relevant data from various online sources. Whether it's finding answers to specific questions or accessing the latest updates, users can rely on WebChat AI to deliver accurate and up-to-date information instantly.

2. **OpenAI GPT-3.5 Powered:** Powered by OpenAI's cutting-edge GPT-3.5 model, WebChat AI is equipped with advanced natural language processing capabilities. This enables the chatbot to understand complex queries, infer context, and generate human-like responses with unparalleled accuracy and fluency.

3. **Customizable Interface:** WebChat AI offers a user-friendly and customizable interface that enhances the overall user experience. With features such as customizable chat themes, font styles, and emoticon support, users can personalize their chat environment to suit their preferences and style.

4. **Multi-platform Support:** Whether it's on desktop, mobile, or tablet devices, WebChat AI provides a seamless cross-platform experience. Users can access the chatbot application from anywhere, anytime, ensuring convenient access to information and assistance whenever needed.

With WebChat AI, we're transforming the way users engage with online content. Our goal is to empower users with intelligent conversational agents that provide instant access to information, streamline decision-making processes, and enhance overall productivity and convenience.

## How to Start the Service

To start the WebChat service, follow these steps:

1. **Create an .env file:** Create a file named `.env` in the root directory of the project and add the following environment variables:

    ```
    OPENAI_API_KEY=<your_OpenAI_API_key>
    SERPER_API_KEY=<your_Google_Serper_API_key>
    MODEL_SETTINGS={"model_name": "<name_of_the_model>", "streaming": "<True_or_False>"}
    LANGCHAIN_API_KEY=<your_Langchain_API_key>
    REDIS_URL=<your_Redis_URL>
    ```

    Replace `<your_OpenAI_API_key>`, `<your_Google_Serper_API_key>`, `<name_of_the_model>`, `<True_or_False>`, `<your_Langchain_API_key>`, and `<your_Redis_URL>` with your actual API keys and URLs.

2. **Install Requirements:** Install the required Python packages by running the following command in your terminal:

    ```
    pip install -r requirements.txt
    ```

3. **Run the Service:** Start the service using the following command:

    ```
    uvicorn app.router:app --reload
    ```

    This command will launch the FastAPI application, and the service will be accessible at `http://localhost:8000`.




