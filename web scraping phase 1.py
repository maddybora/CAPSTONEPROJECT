#!/usr/bin/env python
# coding: utf-8

# In[3]:


sudo apt-get install python3-pip


# In[4]:


import sys
sys.version


# In[5]:


get_ipython().system('pip install requests')


# In[6]:


import sys
sys.version


# In[7]:


pip install requests


# In[1]:


import requests
from bs4 import BeautifulSoup
import csv

# Define the URL for a city (e.g., Sydney)
url = "https://www.booking.com/city/sydney.html"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Extract hotel details (example)
hotel_name = soup.find("h2", class_="sr-hotel__name").text
location = soup.find("span", class_="jq_tooltip").text
num_reviews = soup.find("div", class_="reviewFloater").text
user_rating = soup.find("div", class_="bui-review-score__badge").text
star_rating = soup.find("span", class_="review-score-badge").text
review_score = soup.find("div", class_="bui-review-score__text").text

# Save data to CSV file
with open('Data1.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["sno", "Hotel name", "cities", "location", "number of reviews", "user ratings", "star rating", "review score"])
    writer.writerow([1, hotel_name, "Sydney", location, num_reviews, user_rating, star_rating, review_score])


# In[2]:


pip install beautifulsoup4


# In[3]:


from bs4 import BeautifulSoup


# In[15]:


import requests
from bs4 import BeautifulSoup
import csv


cities = [
    {"name": "Dubai, United Arab Emirates", "url": "https://www.booking.com/city/dubai.html"},
    {"name": "London, United Kingdom", "url": "https://www.booking.com/city/london.html"},
    {"name": "Kuala Lumpur, Malaysia", "url": "https://www.booking.com/city/kuala-lumpur.html"},
    {"name": "Manchester", "url": "https://www.booking.com/city/manchester.html"},
    {"name": "New Delhi", "url": "https://www.booking.com/city/new-delhi.html"},
    {"name": "Birmingham", "url": "https://www.booking.com/city/birmingham.html"},
    {"name": "Berlin", "url": "https://www.booking.com/city/berlin.html"},
    {"name": "Sydney", "url": "https://www.booking.com/city/sydney.html"},
    {"name": "Melbourne", "url": "https://www.booking.com/city/melbourne.html"},
    {"name": "Paris", "url": "https://www.booking.com/city/paris.html"},
    {"name": "Tokyo", "url": "https://www.booking.com/city/tokyo.html"},
    {"name": "Toronto", "url": "https://www.booking.com/city/toronto.html"},
]


with open('Data1.csv', 'w', newline='', encoding='utf-8') as data1_file:
    data1_writer = csv.writer(data1_file)
    data1_writer.writerow(["sno", "Hotel name", "cities", "location", "number of reviews", "user ratings", "star rating", "review score"])


for sno, city_info in enumerate(cities, start=1):
    city_name = city_info["name"]
    city_url = city_info["url"]

  
    response = requests.get(city_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        
        hotel_name = soup.find("h2", class_="sr-hotel__name").text
    except AttributeError:
        hotel_name = "N/A"

    try:
        location = soup.find("span", class_="jq_tooltip").text
    except AttributeError:
        location = "N/A"

    try:
        num_reviews = soup.find("div", class_="reviewFloater").text
    except AttributeError:
        num_reviews = "N/A"

    try:
        user_ratings = soup.find("div", class_="bui-review-score__badge").text
    except AttributeError:
        user_ratings = "N/A"

    try:
        star_rating = soup.find("span", class_="review-score-badge").text
    except AttributeError:
        star_rating = "N/A"

    try:
        review_score = soup.find("div", class_="bui-review-score__text").text
    except AttributeError:
        review_score = "N/A"

    with open('Data1.csv', 'a', newline='', encoding='utf-8') as data1_file:
        data1_writer = csv.writer(data1_file)
        data1_writer.writerow([sno, hotel_name, city_name, location, num_reviews, user_ratings, star_rating, review_score])

    print(f"Scraped data for {city_name}")

print("Web scraping for all cities is complete.")


# In[ ]:




