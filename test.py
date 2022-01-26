"""
from charset_normalizer import api
import requests

api_key = "d84cac5344msh33270a08a1f925dp1a6804jsnc0e11ff8cd25"

url = "https://hotels4.p.rapidapi.com/properties/list"

querystring = {"destinationId":"1489365","pageNumber":"1","pageSize":"25","checkIn":"2020-01-08","checkOut":"2020-01-15","adults1":"1","sortOrder":"PRICE","locale":"en_US","currency":"USD"}

headers = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': api_key
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
"""
dateInterval = "01/25/2022 - 01/25/2022"
dates = dateInterval.split(" - ")
checkin = dates[0].replace("/", "-")
checkIn = checkin[6:10] + "-" + checkin[0:2] + "-" + checkin[3:5]
print(checkIn)