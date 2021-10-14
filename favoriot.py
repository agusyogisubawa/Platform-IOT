import requests
import time
import json
import random

APIKEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFndXN5b2dpIiwicmVhZF93cml0ZSI6dHJ1ZSwiaWF0IjoxNTg4MTU2NzkwfQ.ggM0zc3F2zNQihGo9A1r732e0BIRabb9jOuX1p8lOxs"
DEVICE_DEV_ID = "Test@agusyogi"

url = "https://apiv2.favoriot.com/v2/streams"

headers = {
    'apikey': APIKEY,
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "b404ce24-2b0b-b9c8-8895-6324a6900c47"
}

while True:
    for bil in range(40):
        root = {}
        root["device_developer_id"] = DEVICE_DEV_ID
        data = {}
        bil = random.randint(20, 50)
        data["Temperature"] = bil
        root["data"] = data
        body = json.dumps(root)
        print(body)
        response = requests.request("POST", url, headers=headers, data=body)
        print(response.text)
        print("")
        time.sleep(3)
