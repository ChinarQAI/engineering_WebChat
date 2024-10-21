# import os
#
# from langchain_redis import RedisConfig, RedisVectorStore
# from langchain_openai import OpenAIEmbeddings
#
# embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
#
# config = RedisConfig(
#     index_name="cqai_chat",
#     redis_url=os.environ.get("REDIS_URL"),
#     metadata_schema=[
#         {"name": "category", "type": "tag"},
#     ],
# )
#
# vector_store = RedisVectorStore(embeddings, config=config)