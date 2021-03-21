## Overview

This Flask application contains the basic booking management functionality (create and return bookings for a clinic/servive).

The app is currently deployed on heroku. code is on [github](https://github.com/realCarmineIRL/bookings)

## How to Run

In the top-level directory:

please use API URL and API KEY provided in email

## Installation Instructions

Pull down the source code from this GitLab repository:

````sh
$ git clone git@github.com:realCarmineIRL/bookings.git```
````

Create a new virtual environment:

```sh
$ cd bookings
$ python -m venv ./venv
```

Activate the virtual environment:

```sh
$ source venv/bin/activate
```

Install the python packages in requirements.txt:

```sh
(venv) $ pip install -r requirements.txt
```

Set the file that contains the Flask application and specify that the development environment should be used:

```sh
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ export ENVIRONMENT=flask.cfg
$ export API_URL="(email sent by Domenico to me)"
$ export API_KEY="(email sent by Domenico to me)"
$ flask run
```

Run development server to serve the Flask application:

```sh
(venv) $ flask run
```

Creating a new booking locally

```sh
curl --location --request POST 'http://0.0.0.0:5000/bookings' \
--header 'Content-Type: application/json' \
--data-raw '{
    "clinicId": "clinic100",
    "customerId": "ab123",
    "serviceId": "ser100",
    "date": "2021-01-25",
    "startTime": "T11:00:00"
}'
```

Returning bookings for a clinic locally

```sh
curl --location --request GET 'http://0.0.0.0:5000/clinic/clinic100/bookings' \
--header 'Content-Type: application/json'
```

Creating a new booking Cloud (Heroku)

```sh
curl --location --request POST 'https://booking-system-tc.herokuapp.com/bookings' \
--header 'Content-Type: application/json' \
--data-raw '{
    "clinicId": "clinic100",
    "customerId": "ab123",
    "serviceId": "ser100",
    "date": "2021-01-25",
    "startTime": "T11:00:00"
}'
```

Returning bookings for a clinic Cloud (Heroku)

```sh
curl --location --request GET 'https://booking-system-tc.herokuapp.com/clinic/clinic100/bookings' \
--header 'Content-Type: application/json'
```

## Key Python Modules Used

- Flask
- pytest
- SQLAlchemy
- Flask-Migrat
- Flask-SQLAlchemy
- Flask-Script
- Requests
- gunicorn

This application is written using Python 3.6.

## Testing

To run all the tests:

```sh
(venv) $ python -m pytest -v
```

## Future Development

If I had more time these are the extra features I could add to the app

- Option to update booking
- Option to cancel booking
- Add endpoint to retrieve bookings for a service in a clinic
- Add endpoint to retrieve all bookings for a customer
- Add booking confirmations mesages
- Add Booking reminders
- Add more effective/efficient tests

## Deployment to the Heroku

Deployment method Github master branch with option to wait for CI to pass before deploy enabled.

flow:

- Code get merged into master branch
- Travis-CI runs tests
- if tests pass Heroku starts deployment:
  - runs db migrations
  - deploy the app

## Assumptions

- timeslots are 30min.
- ClinicId, ServiceId and CustomerId and startTime should always be present in post request.
- customer can book same service multiple slots in a day but not rebook a current booked slot.

## Notes

- test_routes.py is disabled because I was having issues with Travis-CI and SQLite as it seems not supported for flask apps only for ruby and rails as per their documentation, the tests pass locally.
