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

Creating a new booking

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

Returning bookings for a clinic

```sh
curl --location --request GET 'http://0.0.0.0:5000/clinic/clinic100/bookings' \
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

## Assumptions

- timeslots are 30min.
- customer can book same service multiple slots in a day but not rebook a current booked slot.
