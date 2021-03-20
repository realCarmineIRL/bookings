from project.models import Booking


def test_new_booking():

    booking = Booking('clinic100', 'ab123', 'ser100', '2021-01-25', 'T09:30:00', 'T10:00:00')

    assert booking.clinic_id == 'clinic100'
    assert booking.customer_id == 'ab123'
    assert booking.service_id == 'ser100'
    assert booking.date == '2021-01-25'
    assert booking.start_time == 'T09:30:00'
    assert booking.end_time == 'T10:00:00'
