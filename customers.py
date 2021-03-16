import requests

def get_customer(customer_id):
  url = f'https://mj2fqlv9ta.execute-api.eu-west-1.amazonaws.com/calicchioc/customers/{customer_id}'

  payload={}
  headers = {
    'Accept': 'application/json',
    'x-api-key': ''
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  # {"customerId":"ab123","firstName":"John","lastName":"Doe","mobile":871229345}
  return response.json()