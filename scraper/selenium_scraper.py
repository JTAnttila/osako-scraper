from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from ..db.mongo_client import collection
from ..config.settings import restaurant_urls
from bs4 import BeautifulSoup
from ..db.mongo_client import save_to_mongodb

def scrape_with_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service('/path/to/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(10)
    html = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html, 'html.parser')
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

def run_selenium_scraper():
    for restaurant_name, url in restaurant_urls.items():
        menu_items = scrape_with_selenium(url)
        save_to_mongodb(menu_items, restaurant_name)