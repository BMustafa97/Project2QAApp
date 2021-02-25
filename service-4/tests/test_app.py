import sys
sys.path.append('/Users/Admin----')   #alter with path changes
from app import app, db, Todo
import unittest
from flask import url_for
from flask_testing import TestCase

class TestBase(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] ="sqlite:///testdb.sqlite"
        return app
    # Pass in configurations for test database
    def setUp(self):
        db.drop_all()
        db.create_all()
        #sample data
     

    #  Will be called before every test

    def tearDown(self):
        db.drop_all()

class TestPages(TestBase):
    def test_home(self):
        response = self.client.get(url_for('/product'))
        self.assertEqual(response.status_code, 200)
