from app import register_user
from flask import Flask, jsonify, request
import unittest
import json
class ApiTestCase(unittest.TestCase):
    def test_register_user(self):
        result = json.loads(register_user())
        self.assertIsInstance(result['users'], list)
