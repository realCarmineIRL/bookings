import requests

def get_clinic(clinic_id):
  url = f'https://mj2fqlv9ta.execute-api.eu-west-1.amazonaws.com/calicchioc/clinics/{clinic_id}'

  payload={}
  headers = {
    'Accept': 'application/json',
    'x-api-key': ''
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  # {'clinicId': 'clinic100', 'city': 'London', 'country': 'United Kingdom', 'streetAddress': '56, Haughton Rd'}
  return response.json()