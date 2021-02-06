from django.test import TestCase


def add_numbers(x, y):
    """Adds two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Tests that the values are added together"""
        self.assertEqual(add_numbers(5, 5), 10)

    def test_subtract_numbers(self):
        """Tests that the values get subtracted"""
        self.assertEqual(subtract(5, 3), 2)
