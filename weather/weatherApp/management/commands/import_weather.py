from django.core.management.base import BaseCommand, CommandError
from weatherApp.models import Weather
import requests, math

class Command(BaseCommand):

	help = "This event would be run daily by crontab for leave to be carried over the next year if the current day is the first day of the year"

	def handle(self, *args, **options):
		
		response = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=3369157&APPID=ba9823fe55ca44bd511816e4e17e6793")
		content = response.json()["list"]

		for entry in content:
			date = entry["dt_txt"]
			wind = entry["wind"]["speed"]
			min_temp = entry["main"]["temp_min"]
			max_temp = entry["main"]["temp_max"]
			rain = entry["weather"][0]["description"]

			# convert wind speed to km/h
			wind = round(wind * 3.6, 2)
			# convert temperature to celcius
			min_temp = round(min_temp - 273, 2)
			max_temp = round(max_temp - 273, 2)

			obj, created = Weather.objects.update_or_create(date=date, defaults={'wind' : wind, 'min_temp' : min_temp, 
				'max_temp' : max_temp, 'rain' : rain})

			obj.save()
		