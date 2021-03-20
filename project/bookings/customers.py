import os
import requests

API_URL = os.environ.get('API_URL')
API_KEY = os.environ.get('API_KEY')

def get_customer(customer_id):
  """
  Returns customer info from api.
  """
  url = f'{API_URL}/customers/{customer_id}'

  payload={}
  headers = {
    'Accept': 'application/json',
    'x-api-key': f'{API_KEY}'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  
  if response.status_code == 404:
    response = {}
    response['MSG'] = 'Customer must exists'
    return response, 404

  # {"customerId":"ab123","firstName":"John","lastName":"Doe","mobile":871229345}
  return response.json(), response.status_code