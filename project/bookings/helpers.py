# Helper functions


def get_timeslots(start_date, end_date, delta):

    current = start_date
    while current < end_date:
        yield current
        current += delta


def get_booked_timeslots(timeslots):
    services_booked = []

    for row in timeslots:
        start_time, end_time = row

        services_booked.append(start_time)

    return services_booked
