# import redis
# import numpy as np

# # Connect to Redis
# r = redis.Redis(
#   host='redis-16011.c244.us-east-1-2.ec2.redns.redis-cloud.com',
#   port=16011,
#   password='vtoZDZxJrC1D20yWKBZc5EKSEJF5e01k')

# # Retrieve and decode embedding
# stored_embedding = r.hget("text_embedding:0", "embedding")
# embedding_array = np.frombuffer(stored_embedding, dtype=np.float32)

# print(embedding_array)



import redis
import numpy as np

# Connect to Redis
r = redis.Redis(
  host='redis-16011.c244.us-east-1-2.ec2.redns.redis-cloud.com',
  port=16011,
  password='vtoZDZxJrC1D20yWKBZc5EKSEJF5e01k')

# Retrieve the embedding from Redis
stored_embedding = r.hget("text_embedding:0", "embedding")

# Convert the stored bytes back into a NumPy array (ensure correct dtype)
embedding_array = np.frombuffer(stored_embedding, dtype=np.float32)

print("Retrieved embedding from Redis:", embedding_array)
