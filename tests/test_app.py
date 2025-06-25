import unittest
import json
from app.app import app, users


class UserApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        # Reset in-memory users before each test
        users.clear()
        users[1] = {"id": 1, "name": "Alice", "email": "alice@example.com"}
        users[2] = {"id": 2, "name": "Bob", "email": "bob@example.com"}

    def test_get_all_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 2)

    def test_get_single_user(self):
        response = self.client.get('/users/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], "Alice")

    def test_get_user_not_found(self):
        response = self.client.get('/users/99')
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        new_user = {"name": "Charlie", "email": "charlie@example.com"}
        response = self.client.post('/users', json=new_user)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['name'], "Charlie")
        self.assertIn('id', data)

    def test_create_user_invalid(self):
        response = self.client.post('/users', json={"name": "Incomplete"})
        self.assertEqual(response.status_code, 400)

    def test_update_user(self):
        update = {"name": "Alice Updated"}
        response = self.client.put('/users/1', json=update)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], "Alice Updated")

    def test_delete_user(self):
        response = self.client.delete('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(1, users)

    def test_delete_nonexistent_user(self):
        response = self.client.delete('/users/999')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
