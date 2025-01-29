import requests
from bs4 import BeautifulSoup
from ..db.mongo_client import collection
from ..config.settings import restaurant_urls

def scrape_restaurant_menu(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the page: {url}")
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    menu_items = []
    for item in soup.select('.menu-item'):
        name = item.select_one('.item-name').get_text(strip=True)
        price = item.select_one('.item-price').get_text(strip=True)
        description = item.select_one('.item-description').get_text(strip=True) if item.select_one('.item-description') else ''
        
        menu_items.append({
            'name': name,
            'price': price,
            'description': description
        })
    
    return menu_items

def save_to_mongodb(menu_items, restaurant_name):
    if menu_items:
        for item in menu_items:
            item['restaurant'] = restaurant_name
            collection.insert_one(item)
        print(f"Successfully saved {len(menu_items)} items for {restaurant_name}.")
    else:
        print(f"No menu items found for {restaurant_name}.")

def run_scraper():
    for restaurant_name, url in restaurant_urls.items():
        menu_items = scrape_restaurant_menu(url)
        save_to_mongodb(menu_items, restaurant_name)