import os
import requests

API_URL = os.environ.get('API_URL')
API_KEY = os.environ.get('API_KEY')

def get_clinic(clinic_id):
  url = f'{API_URL}/clinics/{clinic_id}'

  payload={}
  headers = {
    'Accept': 'application/json',
    'x-api-key': f'{API_KEY}'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  # {'clinicId': 'clinic100', 'city': 'London', 'country': 'United Kingdom', 'streetAddress': '56, Haughton Rd'}
  return response.json()