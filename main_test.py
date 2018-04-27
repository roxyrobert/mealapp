from app import app
from unittest import TestCase
from flask import unittest
from flask_testing import TestCase


class MainTest(unittest.TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        self.app_context = app.app_context()
        self.app_context.push()
        self.client = app.test_client()
        return app
        
    def setUp(self):
        pass

    def test_login(self):
        response = self.client.get("/get_meals")
        self.assert200()
        self.assertTrue("ash", )



