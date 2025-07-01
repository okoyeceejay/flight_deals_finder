from flight_search import FlightSearch
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os, requests
load_dotenv()
fs = FlightSearch()

now = datetime.now()
six_months = now + timedelta(days=6*30)
date_now_formatted = now.strftime(format="%Y-%m-%w")
six_months_date_formatted = six_months.strftime("%Y-%m-%d")

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.flight_data_endpoint = os.getenv("AMADEUS_FLIGHT_SEARCH_API")
        self.currency_code = "GBP"
        self.price = ""
        self.departure_airport_code = "LON"
        self.token = fs.token

    def find_cheapest_flight(self, destination_iata_code, max_price):
        header = {"Authorization": f"Bearer {self.token}"}
        payload = {
            "originLocationCode" : f"{self.departure_airport_code}",
            "destinationLocationCode": f"{destination_iata_code}",
            "departureDate": f"{date_now_formatted}",
            "currencyCode": f"{self.currency_code}",
            "adults": 1,
            "maxPrice": int(max_price),
            "max": 15
        }
        response = requests.get(url=self.flight_data_endpoint, params=payload, headers=header)
        print(response.text)
        response.raise_for_status()
        data = response.json()
        print(data)