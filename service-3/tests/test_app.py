import sys
from app import app
import unittest
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///testdb.sqlite"
        return app
    # Pass in configurations for test database
#class TestPages(TestBase):
#    def test_home(self):
#        response = self.client.get(url_for('slogans'))
#        self.assertEqual(response.status_code, 200)

class TestCase(TestBase):
    def test_get(self):
        with patch("requests.get") as g:
                g.return_value.text = "We're always on your mind."
                response = self.client.get(url_for("sloganstest"))
                self.assertIn(b"We're always on your mind.", response.data)