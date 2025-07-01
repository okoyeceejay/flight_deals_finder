import requests, os
from dotenv import load_dotenv
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.iata_code_data = []
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_API_SECRET")
        self.header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        self.token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.token =self._get_new_token()


    def _get_new_token(self):
        response = requests.post(url=self.token_endpoint, data=self.body, headers=self.header)
        data = response.json()["access_token"]
        return data


    def get_flight_info(self, city):
        header = {"Authorization": f"Bearer {self.token}"}
        flight_info_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        params = {
            "keyword" : city["city"],
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=flight_info_endpoint, params=params, headers=header)
        data = response.json()["data"][0]["iataCode"]
        return data

