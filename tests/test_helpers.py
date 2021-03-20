import project.bookings.helpers as helpers
from datetime import datetime, timedelta


def test_get_timeslots():

    start_time = datetime.strptime(f'2021-01-25T09:00:00', '%Y-%m-%dT%H:%M:%S')
    end_time = datetime.strptime(f'2021-01-25T12:00:00', '%Y-%m-%dT%H:%M:%S')

    results = [dt.strftime('T%H:%M:%S') for dt in helpers.get_timeslots(start_time, end_time, timedelta(minutes=30))]

    assert results == ['T09:00:00', 'T09:30:00', 'T10:00:00', 'T10:30:00', 'T11:00:00', 'T11:30:00']

    print(results)



def test_get_booked_timeslots():
    timeslots = [('T09:00:00', 'T09:30:00'),('T09:30:00', 'T10:00:00')]

    results = helpers.get_booked_timeslots(timeslots)
    
    assert results == ['T09:00:00', 'T09:30:00']