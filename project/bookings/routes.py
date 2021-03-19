# bookings.py
import os
from flask import request, jsonify


from flask import render_template, request, flash, redirect, url_for

from . import bookings_blueprint

from project.models import Booking
from project import db


from . import customers as cs
from . import clinics as cls
from . import services as ss
from . import services_timeslots as st


@bookings_blueprint.route('/bookings', methods=['POST'])
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

    # new_booking = Booking(clinic["clinicId"], customer_id, service_id, date, start_time, start_time)
    # db.session.add(new_booking)
    # db.session.commit()

    
    response["MESSAGE"] = f'Booking for customer: {customer["firstName"]} {customer["lastName"]} for service: {service_id} in clinic: {clinic["clinicId"]} was successful'
    response["status_code"] = 200

    # # Return the response in json format
    return jsonify(response)
    

@bookings_blueprint.route('/clinic/<clinic_id>/bookings', methods=['GET'])
def clinic_bookings(clinic_id):
    response = {}

    # query = db.session.query(Booking.clinic_id, Booking.customer_id, Booking.service_id).filter(Booking.clinic_id == clinic_id).order_by(Booking.clinic_id)
    # Will return all bookings for a clinic
    # # Return the response in json format
    response["status_code"] = 200
    return jsonify(response)
