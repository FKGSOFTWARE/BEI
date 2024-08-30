import requests
import random

def test_random_scotland_city_elevation():
    cities_in_scotland = [
        {"name": "Edinburgh", "lat": 55.9533, "lng": -3.1883},
        {"name": "Glasgow", "lat": 55.8642, "lng": -4.2518},
        {"name": "Aberdeen", "lat": 57.1497, "lng": -2.0943},
        {"name": "Dundee", "lat": 56.4620, "lng": -2.9707},
        {"name": "Inverness", "lat": 57.4778, "lng": -4.2247},
        {"name": "Stirling", "lat": 56.1165, "lng": -3.9369},
        {"name": "Perth", "lat": 56.3962, "lng": -3.4390},
        {"name": "Dumfries", "lat": 55.0707, "lng": -3.6045},
        {"name": "Falkirk", "lat": 56.0010, "lng": -3.7833},
        {"name": "Kilmarnock", "lat": 55.6117, "lng": -4.4958}
    ]

    city = random.choice(cities_in_scotland)
    lat = city["lat"]
    lng = city["lng"]
    api_url = f"https://api.opentopodata.org/v1/test-dataset?locations={lat},{lng}"

    response = requests.get(api_url)
    assert response.status_code == 200, f"API request failed with status code {response.status_code}"

    data = response.json()
    assert "results" in data, "Response JSON does not contain 'results' key"
    elevation = data["results"][0]["elevation"]
    print(f"Elevation for {city['name']} is {elevation} meters")

if __name__ == "__main__":
    test_random_scotland_city_elevation()
