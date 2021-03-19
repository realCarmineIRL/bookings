from project import db


class Booking(db.Model):

    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    clinic_id = db.Column(db.String, nullable=False)
    customer_id = db.Column(db.String, nullable=False)
    service_id = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False)


    def __init__(self, clinic_id, customer_id, service_id, date, start_time, end_time):

        self.clinic_id = clinic_id
        self.customer_id = customer_id
        self.service_id = service_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
