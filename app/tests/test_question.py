import unittest
from app import create_app
import json

class TestQuestion(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.question_data = {
            "createdBy" : 1,
            "meetup" : 2,
            "title" : "question1",
            "body" : "When is the event and where is it being held?"
        }
    def test_get_questions(self):
        """Testing getting all questions."""

        response = self.client.get('/api/question')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_create_question(self):
        """Testing posting a question."""

        response = self.client.post(
            '/api/question', data=json.dumps(self.question_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_question_downvote(self):
        """Testing downvoting a question."""

        response = self.client.get('/api/question/downvote/1')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_no_question_downvote(self):
        """Testing downvoting a question that is not there."""

        response = self.client.get('/api/question/downvote/10')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)
    def test_question_upvote(self):
        """Testing upvoting a question."""

        response = self.client.get(
            '/api/question/upvote/1')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_no_question_upvote(self):
        """Testing upvoting a question that is not there."""

        response = self.client.get('/api/question/upvote/10')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 404)



if __name__ == '__main__':
    unittest.main()
