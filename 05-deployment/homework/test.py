import requests

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

url = "http://localhost:9696/predict"
response = requests.post(url, json=client)
print(response.json())