"""Тестирование главного модуля"""
# В разработке.

import unittest


class BasicTests(unittest.TestCase):
    def test_index(self):
        self.assertEqual(1 + 1, 2)
