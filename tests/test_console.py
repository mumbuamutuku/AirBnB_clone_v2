#!/usr/bin/python3
""" Module for testing console"""
import unittest
import MySQLdb
from console import HBNBCommand
from models import storage
from unittest.mock import patch
import os
import io
import pep8


class TestConsole(unittest.TestCase):
    """Test cases for the console.py module"""

    def test_create_with_params(self):
        # Test creating a User instance with parameters
        self.assertFalse(run_command('User.count()'))
        output = run_command('create User name="John_Doe" age=30')
        self.assertTrue(output.startswith('User.'))
        self.assertTrue(run_command('User.count()'))
        user_id = output.split('.', 1)[1]
        user = storage.get('User', user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.age, 30)

        # Test creating a Place instance with parameters
        self.assertFalse(run_command('Place.count()'))
        output = run_command('create Place '
                             'city_id="1234" '
                             'name="My House" '
                             'price=100.0')
        self.assertTrue(output.startswith('Place.'))
        self.assertTrue(run_command('Place.count()'))
        place_id = output.split('.', 1)[1]
        place = storage.get('Place', place_id)
        self.assertIsNotNone(place)
        self.assertEqual(place.city_id, '1234')
        self.assertEqual(place.name, 'My House')
        self.assertEqual(place.price, 100.0)

    def test_pep8(self):
        """Check console to be pep8 compliant"""
        fchecker = pep8.Checker("console.py", show_source=True)
        file_errors = fchecker.check_all()
        self.assertEqual(file_errors, 0)
