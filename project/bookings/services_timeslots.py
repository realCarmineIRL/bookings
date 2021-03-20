import os
import requests
from datetime import datetime, timedelta

from . import helpers

API_URL = os.environ.get('API_URL')
API_KEY = os.environ.get('API_KEY')

def get_service_timeslots(clinic_id, service_id, requested_date, requested_time):
  url = f'{API_URL}/clinics/{clinic_id}/services/{service_id}/timeslots/{requested_date}'

  payload={}
  headers = {
    'Accept': 'application/json',
    'x-api-key': f'{API_KEY}'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  time_blocks = response.json()

  #   [
  #     {
  #         "startTime": "T08:00:00",
  #         "endTime": "T12:30:00"
  #     },
  #     {
  #         "startTime": "T13:00:00",
  #         "endTime": "T15:30:00"
  #     },
  #     {
  #         "startTime": "T16:00:00",
  #         "endTime": "T18:30:00"
  #     }
  # ]

  for time_block in time_blocks:

    start_time = datetime.strptime(f'{requested_date}{time_block["startTime"]}', '%Y-%m-%dT%H:%M:%S')
    end_time = datetime.strptime(f'{requested_date}{time_block["endTime"]}', '%Y-%m-%dT%H:%M:%S')

    timeslots = [dt.strftime('T%H:%M:%S') for dt in helpers.get_timeslots(start_time, end_time, timedelta(minutes=30))]
    
    if requested_time in timeslots:
      available_slot = True
      break

  return available_slot
