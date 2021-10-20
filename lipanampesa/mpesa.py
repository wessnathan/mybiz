import requests

from myBiz import cred
from myBiz.cred import passKey_Formated
from datetime import datetime

unformatted_time = datetime.now()
formated_time = unformatted_time.strftime("%Y%m%d%H%M%S")

def generate_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
    querystring = {"grant_type":"client_credentials"}
    payload = ""
    headers = {
        "Authorization": "Basic SWZPREdqdkdYM0FjWkFTcTdSa1RWZ2FTSklNY001RGQ6WUp4ZVcxMTZaV0dGNFIzaA=="
    }
    resp = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    json_resp = resp.json()
    my_access_token = str(json_resp['access_token'])
    
    return my_access_token




def lipa_na_mpesa():
    access_token = generate_token()
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + access_token
    }
    
    payload = {
        "BusinessShortCode": cred.biz_code,
        "Password": passKey_Formated(cred.biz_pass_key, cred.biz_key),
        "Timestamp": formated_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254759158305,
        "PartyB": cred.biz_code,
        "PhoneNumber": 254759158305,
        "CallBackURL": "http://www.mybiz.com",
        "AccountReference": "MyBizUserAccount",
        "TransactionDesc": "mybiz" 
    }

    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
    print(response.text.encode('utf8'))
    
    
lipa_na_mpesa()