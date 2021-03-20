# bookings.py
import os
from flask import request, jsonify
from datetime import datetime, timedelta


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
    try:
        customer = cs.get_customer(customer_id)
        clinic = cls.get_clinic(clinic_id)
        service = ss.get_service_timeslots(service_id)
        available_slot = st.get_service_timeslots(clinic_id, service_id, date, start_time) # True if requested time matches clinic service times
    except:
        response = {}
        response["ERROR"] = 'Having throuble connecting to API'
        return jsonify(response), 500

    try:
        results = db.session.query(Booking.start_time, Booking.end_time).filter(Booking.clinic_id == clinic_id, Booking.service_id == service_id, Booking.date == date).order_by(Booking.start_time).all()
    except:
        response = {}
        response["ERROR"] = 'Database Error'
        return jsonify(response), 500

    if data["startTime"] in get_booked_timeslots(results):
        response["MESSAGE"] = f'Timeslot requested is not available'
        return jsonify(response), 202

    end_time = datetime.strptime(f'{data["date"]}{data["startTime"]}', '%Y-%m-%dT%H:%M:%S') + timedelta(minutes=30)


    try:
        print(start_time)
        new_booking = Booking(clinic["clinicId"], customer_id, service_id, date, start_time, end_time.strftime('T%H:%M:%S'))
        db.session.add(new_booking)
        db.session.commit()
    except:
        response["ERROR"] = f'Booking for customer: {customer["firstName"]} {customer["lastName"]} for service: {service_id} in clinic: {clinic["clinicId"]} was NOT successful'
        return jsonify(response), 500

    
    response["MESSAGE"] = f'Booking for customer: {customer["firstName"]} {customer["lastName"]} for service: {service_id} in clinic: {clinic["clinicId"]} was successful'
    return jsonify(response), 201
    

@bookings_blueprint.route('/clinic/<clinic_id>/bookings', methods=['GET'])
def clinic_bookings(clinic_id):

    try:
        results = db.session.query(Booking.clinic_id, Booking.customer_id, Booking.service_id, Booking.date, Booking.start_time, Booking.end_time).filter(Booking.clinic_id == clinic_id).order_by(Booking.clinic_id).all()
    except:
        response = {}
        response["ERROR"] = 'Database Error'
        return jsonify(response), 500
    
    response = []

    for row in results:
        item = {}
        clinic_id, customer_id, service_id, date, start_time, end_time = row

        item['clinicId'] = clinic_id
        item['customerId'] = customer_id
        item['serviceId'] = service_id
        item['date'] = date
        item['startTime'] = start_time
        item['endTime'] = end_time

        response.append(item)

    return jsonify(response), 200


def get_booked_timeslots(timeslots):
    services_booked = []

    for row in timeslots:
        start_time, end_time = row

        services_booked.append(start_time)

    return services_booked
