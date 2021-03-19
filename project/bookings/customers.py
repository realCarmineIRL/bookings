import os
import requests

API_URL = os.environ.get('API_URL')
API_KEY = os.environ.get('API_KEY')

def get_customer(customer_id):
  url = f'{API_URL}/customers/{customer_id}'

  payload={}
  headers = {
    'Accept': 'application/json',
    'x-api-key': f'{API_KEY}'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  # {"customerId":"ab123","firstName":"John","lastName":"Doe","mobile":871229345}
  return response.json()