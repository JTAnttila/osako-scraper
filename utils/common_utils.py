import logging

logging.basicConfig(filename='../logs/scraper.log', level=logging.INFO)

def log_message(message):
    logging.info(message)

def handle_error(error):
    logging.error(str(error))