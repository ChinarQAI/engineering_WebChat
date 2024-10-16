import redis
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Step 1: Connect to Redis
r = redis.Redis(
  host='redis-16011.c244.us-east-1-2.ec2.redns.redis-cloud.com',
  port=16011,
  password='vtoZDZxJrC1D20yWKBZc5EKSEJF5e01k')

# Step 2: Fetch the stored data
chinar_quantum_ai_data = r.get('scraped_data')  # Assuming 'scraped_data' is the key you used to store the data

# Step 3: Parse the JSON string back to a Python dictionary
data_dict = json.loads(chinar_quantum_ai_data)

# Step 4: Extract the relevant text information (e.g., title and description)
text_to_embed = f"{data_dict['title']} {data_dict['description']}"

# Step 5: Generate embeddings using SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding = model.encode([text_to_embed])[0]  # Generate embedding for the text

# Step 6: Convert the NumPy array embedding to bytes for Redis storage
embedding_bytes = embedding.tobytes()

# Step 7: Store the embedding in Redis with appropriate keys (Hash to store both text and embedding)
r.hset('text_embedding:chinar', mapping={'text': text_to_embed, 'embedding': embedding_bytes})

print("Embedding for Chinar Quantum AI stored successfully in Redis!")

# Step 8: Retrieve the embedding from Redis
retrieved_embedding = r.hget('text_embedding:chinar', 'embedding')

# Step 9: Convert the stored bytes back into a NumPy array (ensure correct dtype)
embedding_array = np.frombuffer(retrieved_embedding, dtype=np.float32)

print("Retrieved embedding:", embedding_array)
