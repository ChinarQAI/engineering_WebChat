import requests
from bs4 import BeautifulSoup
import redis
import json

# Redis Cloud connection details
redis_host = 'redis-16011.c244.us-east-1-2.ec2.redns.redis-cloud.com'
redis_port = 16011
redis_password = 'vtoZDZxJrC1D20yWKBZc5EKSEJF5e01k'  

# Connect to Redis Cloud
try:
    r = redis.Redis(
        host=redis_host,
        port=redis_port,
        password=redis_password
    )
    # Test connection
    r.ping()
    print("Connected to Redis Cloud")
except redis.ConnectionError as e:
    print(f"Failed to connect to Redis: {e}")

# Function to scrape data from Chinar Quantum AI website
def scrape_chinar_quantum_ai():
    url = 'https://www.chinarquantumai.org/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all text content
        text_content = soup.get_text(separator='\n', strip=True)
        
        # Extract the title
        title = soup.title.string if soup.title else 'No title found'
        
        # Extract meta description
        description = soup.find('meta', attrs={'name': 'description'})
        description_content = description['content'] if description else 'No description found'

        # Store the data
        data = {
            "title": title,
            "description": description_content,
            "content": text_content,
            "url": url
        }

        return data
    else:
        print(f"Failed to retrieve website content. Status code: {response.status_code}")
        return None

# Scrape the data
scraped_data = scrape_chinar_quantum_ai()

# Store scraped data in Redis
if scraped_data:
    try:
        r.set('chinar_quantum_ai_data', json.dumps(scraped_data))
        print("Scraped data saved to Redis Cloud")
    except Exception as e:
        print(f"Error saving data to Redis: {e}")
else:
    print("No data to save to Redis")













# import requests
# from bs4 import BeautifulSoup
# import redis
# import json
# from urllib.parse import urljoin

# # Redis Cloud connection details
# redis_host = 'redis-16011.c244.us-east-1-2.ec2.redns.redis-cloud.com'
# redis_port = 16011
# redis_password = 'vtoZDZxJrC1D20yWKBZc5EKSEJF5e01k'  

# # Connect to Redis Cloud
# try:
#     r = redis.Redis(
#         host=redis_host,
#         port=redis_port,
#         password=redis_password
#     )
#     # Test connection
#     r.ping()
#     print("Connected to Redis Cloud")
# except redis.ConnectionError as e:
#     print(f"Failed to connect to Redis: {e}")

# # Function to scrape data from a given URL
# def scrape_page(url):
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
        
#         # Extract all text content
#         text_content = soup.get_text(separator='\n', strip=True)
        
#         # Extract the title
#         title = soup.title.string if soup.title else 'No title found'
        
#         # Extract meta description
#         description = soup.find('meta', attrs={'name': 'description'})
#         description_content = description['content'] if description else 'No description found'

#         # Store the data
#         data = {
#             "title": title,
#             "description": description_content,
#             "content": text_content,
#             "url": url
#         }

#         return data
#     else:
#         print(f"Failed to retrieve website content. Status code: {response.status_code}")
#         return None

# # Function to find all links on a page
# def find_links(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
#     return links

# # Main function to scrape the entire website
# def scrape_website(base_url):
#     scraped_data = []
#     visited_urls = set()
#     urls_to_visit = [base_url]

#     while urls_to_visit:
#         current_url = urls_to_visit.pop(0)
#         if current_url not in visited_urls:
#             visited_urls.add(current_url)
#             data = scrape_page(current_url)
#             if data:
#                 scraped_data.append(data)
#                 # Find and add new links to visit
#                 new_links = find_links(current_url)
#                 for link in new_links:
#                     if link.startswith(base_url):
#                         urls_to_visit.append(link)

#     return scraped_data

# # Scrape the website
# base_url = 'https://www.chinarquantumai.org/'
# scraped_data = scrape_website(base_url)

# # Store scraped data in Redis
# if scraped_data:
#     try:
#         r.set('chinar_quantum_ai_data', json.dumps(scraped_data))
#         print("Scraped data saved to Redis Cloud")
#     except Exception as e:
#         print(f"Error saving data to Redis: {e}")
# else:
#     print("No data to save to Redis")
