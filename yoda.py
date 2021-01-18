import folium
import webbrowser
import time
import requests
import geopy
from geopy.geocoders import Nominatim

tip = "Baby Yoda on a trip!"
answer = ""
address = []
restart = "yes"

print("Greetings!\n This is a basic web app you can use to spawn a map in a precise location.\n Take baby Yoda on a trip!")

while (restart=="yes"):
	geolocator = Nominatim(user_agent="yoda_app")
	answer = input("pick location: \n >>  ")
	location = geolocator.geocode(answer)

	print((location.latitude, location.longitude))
	address = [location.latitude, location.longitude]

	m = folium.Map(location=address, tiles='CartoDB dark_matter', zoom_start=14)

	# adding a marker in that same location
	avatar = folium.features.CustomIcon('BabyYodaSprite.gif', icon_size=(64, 64))
	folium.Marker(location=address, tooltip=tip, icon=avatar).add_to(m)

	#saving the map as an html fiel in the same app folder
	m.save('map.html')

	print("map generated successfuly.")
	# openning the generatd map in default browser
	time.sleep(1)
	webbrowser.open_new_tab('index.html')
	restart = input("wanna go somwhere else?  < yes / no > \n")
	answer = ""
	if not restart == "yes":
		break