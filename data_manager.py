import requests
import os
from dotenv import load_dotenv
from flight_search import FlightSearch
from pprint import pprint

load_dotenv()
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.put_sheety_data_response = None
        self.header = {"Authorization" : os.getenv("FLIGHT_DEALS_HEADER_AUTH")}
        self.sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
        self.get_sheet_data_response = ""
        self.sheet_data = {}
        self.get_sheety_data()
        self.put_sheety_data_endpoint = os.getenv("SHEETY_DATA_UPDATE_ENDPOINT")
        self.iata_codes = []
        self.get_flight_data()

    def get_sheety_data(self):
        self.get_sheet_data_response = requests.get(url=self.sheety_endpoint, headers=self.header)
        self.get_sheet_data_response.raise_for_status()
        self.sheet_data = self.get_sheet_data_response.json()['prices']
        return self.sheet_data

    def get_flight_data(self):
        for city in self.sheet_data:
            fs = FlightSearch()
            data = fs.get_flight_info(city)
            self.iata_codes.append(data)

    def update_iata_code(self):
        for city, code in zip(self.sheet_data, self.iata_codes):
            payload = {
                "currency_code": {"iataCode": code}
            }
            response = requests.put(
                url=f"{self.put_sheety_data_endpoint}/{city['id']}",
                headers=self.header,
                json=payload
            )
            response.raise_for_status()