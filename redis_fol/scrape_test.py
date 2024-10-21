# ast_main.py or add a new FastAPI route file (e.g., scrape_api.py)
from fastapi import FastAPI, APIRouter
import requests
from bs4 import BeautifulSoup
import redis
import json

app = FastAPI()
router = APIRouter()

# Redis connection (use environment variables or .env file to hide sensitive information)
redis_host = 'redis-16011.c244.us-east-1-2.ec2.redns.redis-cloud.com'
redis_port = 16011
redis_password = 'vtoZDZxJrC1D20yWKBZc5EKSEJF5e01k'

r = redis.Redis(
    host=redis_host,
    port=redis_port,
    password=redis_password
)

# Function to scrape the Chinar Quantum AI website
def scrape_chinar_quantum_ai():
    url = 'https://www.chinarquantumai.org/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string
        description = soup.find('meta', attrs={'name': 'description'})['content']

        data = {
            "title": title,
            "description": description,
            "url": url
        }

        return data
    else:
        return None

# Scraping API route
@router.get("/scrape")
async def scrape_website():
    scraped_data = scrape_chinar_quantum_ai()

    if scraped_data:
        try:
            # Save scraped data to Redis
            r.set('chinar_quantum_ai_data', json.dumps(scraped_data))
            return {"message": "Scraped data saved to Redis", "data": scraped_data}
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Failed to scrape the website"}

# Route to retrieve scraped data from Redis
@router.get("/get-scraped-data")
async def get_scraped_data():
    try:
        scraped_data = r.get('chinar_quantum_ai_data')
        if scraped_data:
            return json.loads(scraped_data)
        else:
            return {"message": "No data found in Redis"}
    except Exception as e:
        return {"error": str(e)}

# Include the router in the FastAPI app
app.include_router(router)