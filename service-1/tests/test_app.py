import sys
from app import app, db, Generator
import unittest
from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app
    # Pass in configurations for test database
  #  def setUp(self):
  #      db.drop_all()
  #      db.create_all()
        #sample data
#      test_text = Generator(id='1', result='Deli')
 #       db.session.add(test_text)
 #       db.session.commit()

    #  Will be called before every test

   # def tearDown(self):
   #     db.drop_all()

class TestPages(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        

#create a mock test
#class TestService1(TestBase):
#    def test_get(self):
#        response = self.client.get(url_for('home'), follow_redirects=True)
#        self.assertIn(b'Deli', response.data)