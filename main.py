import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://ru.m.wikipedia.org/wiki/Погода"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parse")

temperature = soup.find("div", class_="weather-temp").text

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE weather (date_time TEXT, temp TEXT)")

cursor.execute("INSERT INTO weather VALUES (?, ?)", (now))

print("Данные успешно сохранены!")
