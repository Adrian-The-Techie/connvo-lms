import requests
import json
import random
import uuid
from django.http.response import HttpResponse, JsonResponse
from requests.models import HTTPBasicAuth

def _generateB2CKeys():
        try:
            response = requests.get(
                "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials",
                auth=HTTPBasicAuth(
                    'AM92daVbfPt6xgpcn8w6noh4llKKpJKVu6IAruKNUnbKKVgf',
                    'F4no5NAAY6n8GW4a926cITg8Pl3zGOAPAGJhqVWUs6Qy6R9NYivpcOZcvj3tPr28',
                ),
            )
            formattedResponse = dict(json.loads(response.text))
            return formattedResponse["access_token"]
        except Exception as e:
            return JsonResponse(e)
        

def get_reference_no():
    return uuid.uuid4().hex



def generate_random_number():
    # Generate multiples of 50 within the range 250 to 800
    return random.choice([i for i in range(250, 801, 50)])

def get_phone():
     numberList=['254708753557','254711324691', '' ,'254113011396']

     number=random.choice(numberList)

     return number
        
def disburse():
        url = "https://api.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
        data = {
                "InitiatorName": "gongagongaB2C",
                "SecurityCredential": "KGwZrRsEUyPy4voojebL+HET5o8oFxo0bhVhs5ssbDDU3QJCv17gq6E8UNMVv9eUcpEaKKNYk1g8TQXNJCKDmqEQDcXc5HG0Y1LZ3rdu2GrsSM9RfoJZwQ7Vyt0ppTjLlh5GKHtlUjf4biKNEOkmFUTjKQEKZHKful0knCeHwBNGch25YGozNd6QJzUdD89h195DGrZ8CdWA3GAEnAjEFStscu4lDKz0TrdAJnGuSVgetFBukEMWyqvySpHsK7BL6w+hlwXU6kEBxonqlZus1jULxDt3oVz37r3lOp97frCprwR/hxbuQZaqFcZho6wMpLqtyaqg3FpuZtFKO/6A4w==",
                "CommandID": "PromotionPayment",
                "Amount": "600",
                "PartyA": "3039953",
                "PartyB": "254113011396",
                "Remarks": get_reference_no(),
                "QueueTimeOutURL": "https://webhook.site/433a2fa4-82a9-4a18-90cf-36b7f224a611",
                "ResultURL": "https://webhook.site/433a2fa4-82a9-4a18-90cf-36b7f224a611",
                "Occasion": get_reference_no()
            }

        headers = {
            "Authorization": "Bearer " + _generateB2CKeys(),
            "Content-type": "application/json",
        }
        try:
            r = requests.post(url, json=data, headers=headers)
            response = dict(json.loads(r.text))
            return {"status": 1, "response": response}
        except Exception as e:
            return {"status": 0, "error": e}
        

disburse()