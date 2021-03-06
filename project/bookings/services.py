import os
import requests

API_URL = os.environ.get('API_URL')
API_KEY = os.environ.get('API_KEY')

def get_service(service_id):
  """
  Returns service info from api.
  """
  url = f'{API_URL}/services/{service_id}'

  payload={}
  headers = {
    'Accept': 'application/json',
    'x-api-key': f'{API_KEY}'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  if response.status_code == 404:
    response = {}
    response['MSG'] = 'Service must exists'
    return response, 404

  return response.json(), response.status_code
