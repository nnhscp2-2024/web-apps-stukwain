"""
Name:
Title: Weather App
Description: Make a weather web app using Flask and Openweathermap API
"""
# imports for Flask, API calls, City class
from datetime import datetime
from flask import Flask, request, render_template, redirect, url_for  
import requests
from city import City

# list of City objects
cities = []
API_KEY = None

def get_data(city):
	"""
	Returns API data from a given city string.

	Parameters:
	city (str): The name of the city to fetch data for.

	Returns:
	list: A list of data fetched from the API, with the city name as the first element.
	"""
	# list of data fetched from API
	data = [city.title()]
	# insert code to get API data (Step 3)
	return data

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
	return f"""<h1>Hello, World!</h1> 
 	<p>The date/time is {datetime.now()}.</p>
 	"""

app.run(host='0.0.0.0', port=8080) # any code below 'app.run' line won't run