import time
import requests
import math
import random

TOKEN = "token"
DEVICE_LABEL = "smart-home"  
VARIABLE_LABEL_1 = "temperature"
#VARIABLE_LABEL_2 = "humidity"


def build_payload(variable_1): # variable_2):
    value_1 = random.randint(20, 50)
#    value_2 = random.randint(0, 85)
    payload = {variable_1: value_1} #variable_2: value_2,}
    return payload

def post_request(payload):
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False
    print("[INFO] request made properly, your device is updated")
    return True

def main():
    payload = build_payload(
        VARIABLE_LABEL_1) #, VARIABLE_LABEL_2)
    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")

if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)
