"""Тестирование api version 1"""
# В разработке.

import json
# Донастроить данный импорт для нужного состояния Проекта
from app import create_app
import unittest


class ApiV1TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def test_get_items(self):
        response = self.client.get('/api/v1/items')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_item_by_id(self):
        response = self.client.get('/api/v1/items/1')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)
        self.assertEqual(data['id'], 1)

    def test_404_error(self):
        response = self.client.get('/api/v1/nonexistent_route')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
