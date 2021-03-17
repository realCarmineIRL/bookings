# bookings.py
import os
from flask import Flask, request, jsonify

import customers as cs
import clinics as cls
import services as ss
import services_timeslots as st


app = Flask(__name__)

@app.route('/bookings', methods=['POST'])
def bookings():

    data = request.get_json()
    
    # {
    #   "clinicId": "clinic100",
    #   "customerId": "ab123",
    #   "serviceId": "ser100",
    #   "date": "2021-01-25",
    #   "startTime": "T10:30:00"
    # }

    clinic_id = data['clinicId']
    customer_id = data['customerId']
    service_id = data['serviceId']
    date  = data['date']
    start_time = data['startTime']

    response = {}

    # getting customer information
    customer = cs.get_customer(customer_id)
    clinic = cls.get_clinic(clinic_id)
    service = ss.get_service_timeslots(service_id)
    available_slot = st.get_service_timeslots(clinic_id, service_id, date, start_time) # True if requested time matches clinic service times

    response["MESSAGE"] = f'Booking for customer: {customer["firstName"]} {customer["lastName"]} for service: {service_id} in clinic: {clinic["clinicId"]} was successful'
    response["status_code"] = 200

    # # Return the response in json format
    return jsonify(response)

app = Flask(__name__)

@app.route('/clinic/<clinic_id>/bookings', methods=['GET'])
def clinic_bookings(clinic_id):

    # Will return all bookings for a clinic
    # # Return the response in json format
    return jsonify(response)

@app.route('/clinic/<clinic_id>/services/<service_id>/bookings', methods=['GET'])
def clinic_service_bookings(clinic_id, service_id):

    # Will return all bookings for a specific service in a clinic
    # # Return the response in json format
    return jsonify(response)


@app.route('/')
def index():
    return "<h1>Welcome to Therapie Clinic</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, host="0.0.0.0", port=5000)