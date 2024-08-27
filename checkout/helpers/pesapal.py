import json

import requests
from decouple import config

headers = {"Accept": "application/json", "Content-Type": "application/json"}


def generateToken():
    requestBody = {
        "consumer_key": config("PESAPAL_CONSUMER_KEY"),
        "consumer_secret": config("PESAPAL_CONSUMER_SECRET"),
    }

    res = requests.post(
        "{}/Auth/RequestToken".format(config("PESAPAL_LIVE_ENDPOINT")),
        data=json.dumps(requestBody),
        headers=headers,
    )
    formattedResponse = res.json()

    return formattedResponse["token"]


def submitOrder(request):
    headers["Authorization"] = "Bearer {}".format(generateToken())

    res = requests.post(
        "{}/Transactions/SubmitOrderRequest".format(config("PESAPAL_LIVE_ENDPOINT")),
        data=json.dumps(request),
        headers=headers,
    )

    print(res)

    formattedResponse = res.json()

    # if formattedResponse["status"] == 500:
    #     raise Exception(formattedResponse)

    return formattedResponse


def getTransactionStatus(orderTrackingId):
    headers["Authorization"] = "Bearer {}".format(generateToken())

    res = requests.get(
        "{}/Transactions/GetTransactionStatus".format(config("PESAPAL_LIVE_ENDPOINT")),
        headers=headers,
        params={"orderTrackingId": orderTrackingId},
    )

    return res.json()
