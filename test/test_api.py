import requests
from pprint import pprint

def get_all_bookings():
    """
    Creates a request to fetch all bookings
    """
    response = requests.get("http://localhost:8085/assignment/bookings", json={})
    pprint(response.json())

if __name__ == '__main__':
    get_all_bookings()


