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
        self.tags_meetup_data = {
                	"meetup" : 2,
                	"topic" : "Topic",
                	"tags" : ["programming", "blockchain"]

                }

        self.images_meetup_data = {
                	"meetup" : 2,
                	"topic" : "Topic",
                	"images" : ["image/image.jpg", "image/image1.jpg"],

                }

    def test_get_meetup(self):
        """Testing getting a meetup."""

        response = self.client.get('/api/meetup')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_get_specific_meetup(self):
        """Testing get specific meetup."""

        response = self.client.get('/api/meetup/1')

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

    def test_add_tags_meetup(self):
        """Testing add tags for a meetup."""

        response = self.client.post(
            '/api/meetup/tags', data=json.dumps(self.tags_meetup_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_add_images_meetup(self):
        """Testing add images for a meetup."""

        response = self.client.post(
            '/api/meetup/images', data=json.dumps(self.images_meetup_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)




if __name__ == '__main__':
    unittest.main()
