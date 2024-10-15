# ast_main.py or add a new FastAPI route file (e.g., query_search_api.py)
from fastapi import FastAPI, APIRouter
import redis
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()
router = APIRouter()

# Redis connection
r = redis.Redis(
  host='redis-16011.c244.us-east-1-2.ec2.redns.redis-cloud.com',
  port=16011,
  password='vtoZDZxJrC1D20yWKBZc5EKSEJF5e01k'
)

# Initialize the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Search API route to query Redis-stored embeddings
@router.get("/query")
async def query_embeddings(query_text: str, top_n: int = 3):
    try:
        # Step 1: Generate embedding for the query text
        query_embedding = model.encode([query_text])[0]

        # Step 2: Retrieve all stored embeddings from Redis
        keys = r.keys('text_embedding:*')
        all_embeddings = []
        all_texts = []

        for key in keys:
            # Retrieve the embedding from Redis
            stored_embedding = r.hget(key, 'embedding')
            embedding_array = np.frombuffer(stored_embedding, dtype=np.float32)

            # Retrieve the corresponding text
            stored_text = r.hget(key, 'text').decode('utf-8')

            # Append the retrieved embedding and text to the lists
            all_embeddings.append(embedding_array)
            all_texts.append(stored_text)

        # Step 3: Calculate cosine similarity between the query and stored embeddings
        all_embeddings = np.array(all_embeddings)
        query_embedding = query_embedding.reshape(1, -1)

        # Compute cosine similarities
        similarities = cosine_similarity(query_embedding, all_embeddings).flatten()

        # Step 4: Sort the results by similarity
        sorted_indices = np.argsort(similarities)[::-1]

        # Step 5: Return the most similar results
        results = []
        for idx in sorted_indices[:top_n]:
            results.append({
                "similarity": float(similarities[idx]),
                "text": all_texts[idx]
            })

        return {"query": query_text, "results": results}

    except Exception as e:
        return {"error": str(e)}

# Include the router in the FastAPI app
app.include_router(router)
