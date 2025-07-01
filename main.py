#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_data import FlightData

dm = DataManager()
sheet_data = dm.sheet_data
# dm.update_iata_code()

for city in sheet_data:
    flight_deals = FlightData()
    flight_deals.find_cheapest_flight(destination_iata_code=city["iataCode"],  max_price=city["lowestPrice"])






# for city in sheet_data:
#     fs = FlightSearch(city)
    # city["iataCode"] = fs.city["iataCode"]
# print(fs.city['iataCode'])

# for city in sheet_data:
