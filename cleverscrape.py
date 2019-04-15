from bs4 import BeautifulSoup
import requests
import lxml 
import pandas as pd  

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XLQuVOgzY2w')
soup = BeautifulSoup(page.content, 'lxml')
week = soup.find('div', id='seven-day-forecast-body')
#print(week.prettify())
items = week.find_all('div', class_='tombstone-container')
#period_name = items.find('p', class_='period-name').text 
#desc = items.find('p', class_='short-desc').text 
#temperatures = items.find('p', class_='temp').text 

# Using list comprehention:
period_name = [item.find('p', class_='period-name').text for item in items]
desc = [item.find('p', class_='short-desc').text for item in items] 
temperatures = [item.find('p', class_='temp').text for item in items]

#print(period_name)
#print(desc)
#print(temperatures)

weather_stuff = pd.DataFrame({
    'Period': period_name,
    'Descriptions' : desc,
    'Temperatures' : temperatures, 
})

print(weather_stuff)

weather_stuff.to_csv('LA_weather.csv')
