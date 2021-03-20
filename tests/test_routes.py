# import unittest
# import os
# import json
# from project import create_app, db


# class BookingTestCase(unittest.TestCase):

#     def setUp(self):
#         self.app = create_app('flask_test.cfg')
#         self.client = self.app.test_client
#         self.booking_request = {
#             "clinicId": "clinic100",
#             "customerId": "ab123",
#             "serviceId": "ser100",
#             "date": "2021-01-25",
#             "startTime": "T09:30:00"
#         }

#         with self.app.app_context():
#             db.create_all()

#     def test_booking_creation(self):

#         mimetype = 'application/json'
#         headers = {
#             'Content-Type': mimetype,
#             'Accept': mimetype
#         }

#         res = self.client().post('/bookings', data=json.dumps(self.booking_request), headers=headers)
#         self.assertEqual(res.status_code, 201)
#         assert res.data == b'{\n  "MESSAGE": "Booking for customer: John Doe for service: ser100 in clinic: clinic100 was successful"\n}\n'

#         res = self.client().get('/bookings', data=json.dumps(self.booking_request), headers=headers)
#         self.assertEqual(res.status_code, 405)

#         res = self.client().get('/clinic/clinic100/bookings', headers=headers)
#         self.assertEqual(res.status_code, 200)

#         res = self.client().get('/clinic/clinic10044/bookings', headers=headers)
#         self.assertEqual(res.status_code, 404)

#         res = self.client().post('/clinic/clinic100/bookings', headers=headers)
#         self.assertEqual(res.status_code, 405)

    
#     def tearDown(self):
#         """teardown all initialized variables."""
#         with self.app.app_context():
#             # drop all tables
#             db.session.remove()
#             db.drop_all()
