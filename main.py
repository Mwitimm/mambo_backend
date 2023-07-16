
import requests
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/process-payment', methods=['POST'])
def process_payment():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer EehwqnzqMd9XEP7baUuTpAHgvgWe'
    }

    payload = {
        "BusinessShortCode": "174379",
        "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMwNzE2MTQ1ODM2",
        "Timestamp": "20230716145836",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": "254708374149",
        "PartyB": "174379",
        "PhoneNumber": "254708374149",
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X"
    }

    response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers=headers, json=payload)
    
    return jsonify(response.text)

if __name__ == '__main__':
    app.run()


