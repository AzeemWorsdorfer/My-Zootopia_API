import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """Fetches animal data from the API Ninja based on the animal name"""

    headers = {"X-Api-Key": API_KEY}

    params = {"name": animal_name}   # Define parameters for the API request

    try:
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data for {animal_name}: {e}")
        return []
