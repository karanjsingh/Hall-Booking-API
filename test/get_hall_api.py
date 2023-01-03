import requests
from pprint import pprint

def get_all_halls():
    """
    Creates a request to fetch all bookings
    """
    context={
        "capacity": 50,
        "startTime": "2021-06-27 15:00:00",
        "endTime": "2021-06-27 16:00:00"
    }
    response = requests.post("http://localhost:8085/assignment/halls", json=context)
    pprint(response.json())

if __name__ == '__main__':
    get_all_halls()