import redis
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Connect to Redis
r = redis.Redis(
  host='redis-16011.c244.us-east-1-2.ec2.redns.redis-cloud.com',
  port=16011,
  password='vtoZDZxJrC1D20yWKBZc5EKSEJF5e01k')

# Step 2: Define a query text (user's input)
query_text = "who is junaid akhtar"

# Step 3: Generate embedding for the query
model = SentenceTransformer('all-MiniLM-L6-v2')
query_embedding = model.encode([query_text])[0]

# Step 4: Retrieve all stored embeddings from Redis
keys = r.keys('text_embedding:*')  # Get all keys matching the pattern
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

# Step 5: Calculate cosine similarity between query embedding and stored embeddings
all_embeddings = np.array(all_embeddings)
query_embedding = query_embedding.reshape(1, -1)  # Reshape for cosine_similarity

# Compute cosine similarities
similarities = cosine_similarity(query_embedding, all_embeddings).flatten()

# Step 6: Sort the results by similarity
sorted_indices = np.argsort(similarities)[::-1]  # Sort in descending order
top_n = 3  # Number of top results to return

# Step 7: Display the most similar results
for idx in sorted_indices[:top_n]:
    print(f"Similarity: {similarities[idx]}")
    print(f"Text: {all_texts[idx]}")
    print("-----")
