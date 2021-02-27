import sys
from app import app
import unittest
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app
        
#class TestPages(TestBase):
#    def test_home(self):
#        response = self.client.get(url_for('firstname'))
#        self.assertEqual(response.status_code, 200)

class TestCase(TestBase):
    def test_get(self):
        with patch("requests.get") as g:
                g.return_value.text = "Koolios"
                response = self.client.get(url_for("firstnametest"))
                self.assertIn(b"Koolios", response.data)