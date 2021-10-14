import requests
import time
import json
import random

ACCESS_TOKEN = "riaI8Y1pyLKMslC10Y5X"

url = "https://demo.thingsboard.io/api/v1/{}/telemetry".format(ACCESS_TOKEN)
print(url)
headers = {
    'content-type': "application/json"
}

while True:
    data_temp = {}
    data_temp["Temperature"] = random.randint(20, 50)
    body = json.dumps(data_temp)
    print(body)
    response = requests.request("POST", url, headers=headers, data=body)
    print(response.text)
    print("")