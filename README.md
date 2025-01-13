# **osako-scraper**

**osako-scraper** is a Python-based web scraping tool designed to gather and manage student-focused restaurant information in Oulu, Finland. It uses **Beautiful Soup** for web scraping and **MongoDB** to store and manage the collected data. Additionally, it integrates the **ChatGPT API** to parse, format, and enhance the scraped information for better usability.

---

## **Features**
- **Web Scraping with Beautiful Soup:** Extract lunch menus, student discounts, and restaurant details from various sources.
- **Data Storage in MongoDB:** Efficiently save and manage structured data, ensuring it's ready for use in applications like web or mobile apps.
- **ChatGPT API Integration:** Parse and refine scraped information, such as extracting student discount-specific menus or standardizing menu formats.
- **Periodic Updates:** Automate scraping and updating with scheduled tasks for the latest data.
- **Scalable Design:** Easily extend the scraper to support additional restaurant websites or integrate with other services.

---

## **Use Cases**
- Aggregating lunch menus and student discounts from restaurants in Oulu.
- Serving updated information to apps or websites via MongoDB queries.
- Parsing complex or unstructured menu formats using AI-powered ChatGPT.

---

## **Tech Stack**
- **Beautiful Soup:** For scraping static web content.
- **MongoDB:** As the database to store and manage scraped data.
- **ChatGPT API:** For natural language processing and data enhancement.
- **Python:** The core programming language powering the tool.

---

## **Planned Features**
- **Dynamic Content Scraping:** Support for JavaScript-heavy sites using Selenium or Playwright.
- **API Integration:** Build a REST or GraphQL API to serve scraped data to frontend applications.
- **Advanced Parsing:** Leverage ChatGPT to extract deeper insights, such as identifying allergens or meal categories.
