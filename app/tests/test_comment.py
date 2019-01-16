import unittest
from app import create_app
import json

class TestComment(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.comment_data = {
            "createdBy" : 1,
            "question" : 2,
            "title" : "What is this",
            "body" : "Your question is out of topic?"
        }
    def test_get_comments(self):
        """Testing getting all comments."""

        response = self.client.get('/api/comment')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_create_comment(self):
        """Testing posting a comment."""

        response = self.client.post(
            '/api/comment', data=json.dumps(self.comment_data), content_type='application/json')

        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)



if __name__ == '__main__':
    unittest.main()
