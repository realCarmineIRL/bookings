# bookings.py
import os
from flask import Flask, request, jsonify

import customers as customers
import clinics as clinics



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
    customer = customers.get_customer(customer_id)
    clinic = clinics.get_clinic(clinic_id)

    print(clinic)

    response["MESSAGE"] = f'Booking for customer: {customer["firstName"]} {customer["lastName"]} for service: {service_id} in clinic: {clinic["clinicId"]} was successful'
    response["status_code"] = 200

    # # Return the response in json format
    return jsonify(response)


@app.route('/')
def index():
    return "<h1>Welcome to Therapie Clinic</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, host="0.0.0.0", port=5000)