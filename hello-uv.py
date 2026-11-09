import requests

resp = requests.get("https://httpbin.org/get", params={"q": "test"})
resp.raise_for_status()
print(resp.json())
