# from sentence_transformers import SentenceTransformer
# import redis
# import numpy as np

# # Initialize the model
# model = SentenceTransformer('all-MiniLM-L6-v2')

# # Sample text data
# texts = ["Hello world", "Redis is great", "Vector databases are useful"]

# # Generate embeddings
# embeddings = model.encode(texts)

# # Connect to Redis
# r = redis.Redis(
#   host='redis-16011.c244.us-east-1-2.ec2.redns.redis-cloud.com',
#   port=16011,
#   password='vtoZDZxJrC1D20yWKBZc5EKSEJF5e01k')

# # Store embeddings in Redis
# for i, embedding in enumerate(embeddings):
#     key = f"text_embedding:{i}"
#     r.hset(key, mapping={"text": texts[i], "embedding": embedding.tobytes()})




# Import necessary libraries
from sentence_transformers import SentenceTransformer
import redis
import numpy as np

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample text data
texts = ["Hello world", "Redis is great", "Vector databases are useful"]

# Generate embeddings
embeddings = model.encode(texts)

# Connect to Redis
r = redis.Redis(
  host='redis-16011.c244.us-east-1-2.ec2.redns.redis-cloud.com',
  port=16011,
  password='vtoZDZxJrC1D20yWKBZc5EKSEJF5e01k')

# Store embeddings in Redis
for i, embedding in enumerate(embeddings):
    key = f"text_embedding:{i}"
    # Convert the NumPy array to bytes
    embedding_bytes = embedding.tobytes()
    
    # Store both text and embedding (as bytes) in Redis using a hash
    r.hset(key, mapping={"text": texts[i], "embedding": embedding_bytes})

print("Embeddings stored in Redis successfully!")
