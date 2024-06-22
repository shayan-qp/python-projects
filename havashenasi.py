import requests, json

api_key="9adced7ddff5c6dc7f031455d3dec00e"

base_url="http://api.openweathermap.org/data/2.5/weather?"
 
city_name=input("enter your city : ")

complete_url=base_url+ "appid=" + api_key + "&q=" + city_name + "&units=metric"

r=requests.get(complete_url)

x=r.json()

print(x["main"]["temp"])