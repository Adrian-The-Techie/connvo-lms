import requests


def conversionToKES(price):
    try:

        res = requests.get(
            "https://openexchangerates.org/api/latest.json?app_id=c1a9d366616d400ba252a7920b57bd8d&symbols=KES"
        )
        finalKESRate = res.json()["rates"]["KES"] + 5.00
        finalAmount = finalKESRate * price

        print(finalAmount)

        return finalAmount

    except Exception as e:

        print(e)
