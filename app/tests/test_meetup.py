import unittest
from app import create_app
import json


class TestMeetup(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.meetup_data = {
            "location": "Nairobi",
            "venue": "Nairobi Garage",
            "images": [],
            "topic": "Dev Fest",
            "happeningOn": "12-2-2019",
            "time": "1100",
            "tags": ["programming", "blockchain"],
            "createdBy": 1,
        }
        self.rsvp_meetup_data = {
                	"user" : 2,
                	"meetup" : 2,
                	"response" : 2,

                }

    def test_get_meetup(self):
        """Testing getting a meetup."""

        response = self.client.get('/api/meetup')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_create_meetup(self):
        """Testing posting a meetup."""

        response = self.client.post(
            '/api/meetup/', data=json.dumps(self.meetup_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_rsvp_meetup(self):
        """Testing rsvp for a meetup."""

        response = self.client.post(
            '/api/meetup/rsvp', data=json.dumps(self.rsvp_meetup_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
