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


# In[17]:


import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('your_database.db')

# Create a cursor object
cursor = conn.cursor()

# Execute an SQL query
query = "SELECT * FROM your_table;"
cursor.execute(query)

# Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the database connection
conn.close()


# In[21]:


import sqlite3

# Create or connect to a new SQLite database (replace 'your_database.db' with your desired database name)
conn = sqlite3.connect('data1.db')

# Close the database connection
conn.close()


# In[22]:


import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data1.db')
cursor = conn.cursor()

# Define the table structure (replace 'your_table' and column names with your own)
create_table_query = """
CREATE TABLE IF NOT EXISTS your_table (
    sno INTEGER PRIMARY KEY,
    Hotel_name TEXT,
    City TEXT,
    Location TEXT,
    Num_Reviews TEXT,
    User_Ratings TEXT,
    Star_Rating TEXT,
    Review_Score TEXT
);
"""

# Execute the CREATE TABLE query
cursor.execute(create_table_query)

# Commit the changes and close the database connection
conn.commit()
conn.close()


# In[23]:


import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('data1.db')
cursor = conn.cursor()

# Open the CSV file and import data into the table (replace 'Data1.csv' with your CSV file)
with open('Data1.csv', 'r', newline='', encoding='utf-8') as data_file:
    csv_reader = csv.reader(data_file)
    next(csv_reader)  # Skip the header row
    for row in csv_reader:
        cursor.execute("INSERT INTO your_table (sno, Hotel_name, City, Location, Num_Reviews, User_Ratings, Star_Rating, Review_Score) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", row)

# Commit the changes and close the database connection
conn.commit()
conn.close()


# In[24]:


SELECT *
FROM your_table
WHERE City = 'Sydney' AND CAST(User_Ratings AS DECIMAL) > 5;


# In[25]:


import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data1.db')
cursor = conn.cursor()

# Execute your SQL queries here
query = "SELECT * FROM your_table;"
cursor.execute(query)

# Fetch and print the results
results = cursor.fetchall()
for row in results:
    print(row)

# Close the database connection
conn.close()


# In[6]:


import csv

# Data for Data1.csv (example data, replace with your actual data)
data1 = [
    ["sno", "Hotel name", "cities", "location", "number of reviews", "user ratings", "star rating", "review score"],
    [1, "Hotel A", "Sydney", "Location A", 100, "4.5", "4.0", "8.5"],
    [2, "Hotel B", "London", "Location B", 150, "4.0", "4.5", "8.0"],
    # Add more data rows here
]

# Data for Data2.csv (example data, replace with your actual data)
data2 = [
    ["sno", "Hotel name", "Free wifi", "Family rooms", "Non Smoking Rooms", "Restaurant", "Bar", "Heating", "Lift", "Breakfast Cuisine1", "Breakfast Cuisine2", "Breakfast Cuisine3"],
    [1, "Hotel A", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Continental", "English", "American"],
    [2, "Hotel B", "Yes", "Yes", "Yes", "Yes", "No", "No", "Yes", "Continental", "Italian", "Japanese"],
    # Add more data rows here
]

# Data for Data3.csv (example data, replace with your actual data)
data3 = [
    ["sno", "Hotel name", "Room Type", "Single Bed", "Double bed", "Prices"],
    [1, "Hotel A", "Standard", "Yes", "No", 100],
    [2, "Hotel B", "Suite", "No", "Yes", 200],
    # Add more data rows here
]

# Write data to CSV files
with open('Data1.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)

with open('Data2.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data2)

with open('Data3.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data3)


# In[7]:


import csv

data1 = [
    ["sno", "Hotel name", "cities", "location", "number of reviews", "user ratings", "star rating", "review score"],
    [1, "Hotel A", "Sydney", "Location A", 100, "4.5", "4.0", "8.5"],
    [2, "Hotel B", "London", "Location B", 150, "4.0", "4.5", "8.0"],
    # Add more data rows here
]

with open('Data1.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data1)


# In[15]:


data2 = [
    ["sno", "Hotel name", "Free wifi", "Family rooms", "Non Smoking Rooms", "Restaurant", "Bar", "Heating", "Lift", "Breakfast Cuisine1", "Breakfast Cuisine2", "Breakfast Cuisine3"],
    [1, "Hotel A", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Continental", "English", "American"],
    [2, "Hotel B", "Yes", "Yes", "Yes", "Yes", "No", "No", "Yes", "Continental", "Italian", "Japanese"],
    # Add more data rows here
]

with open('Data2.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data2)


# In[16]:


data3 = [
    ["sno", "Hotel name", "Room Type", "Single Bed", "Double bed", "Prices"],
    [1, "Hotel A", "Standard", "Yes", "No", 100],
    [2, "Hotel B", "Suite", "No", "Yes", 200],
    # Add more data rows here
]

with open('Data3.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data3)


# In[ ]:




