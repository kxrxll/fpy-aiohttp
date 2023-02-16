import requests

response_1 = requests.post(
    "http://127.0.0.1:5001/ads/",
    json={
        "heading": "Something",
        "description": "Some text about something",
        "creator": "Myself"
    }
)

print(response_1.status_code)
ad_id = response_1.json()['id']
print(ad_id)

response_2 = requests.get(f"http://127.0.0.1:5001/ads/{ad_id}")

print(response_2.status_code)
print(response_2.json())

response_3 = requests.delete(f"http://127.0.0.1:5001/ads/{ad_id}")

print(response_3.status_code)
print(response_3.json())
