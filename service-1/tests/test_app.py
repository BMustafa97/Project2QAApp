import sys
from app import app, db, Generator
import unittest
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestPages(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

class TestCase(TestBase):
    def test_get(self):
        with patch("requests.get") as g:
  #          with patch("requests.get") as r:
                g.return_value.text = "Urban"
  #              r.return_value.text = "The Best in Manchester."

                response = self.client.get(url_for("home"))
                self.assertIn(b"Urban", response.data)
        

#create a mock test
#class TestService1(TestBase):
#    def test_get(self):
#        response = self.client.get(url_for('home'), follow_redirects=True)
#        self.assertIn(b'Deli', response.data)