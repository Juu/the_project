import sys
sys.path.insert(0, './app')
from dotenv import load_dotenv
load_dotenv(dotenv_path='./config/env')
import unittest
import app
import os

class TestApp(unittest.TestCase):
    def test_return_ok(self):
        self.assertEqual(app.return_ok(), 'Ok')
    def test_return_secret_env(self):
        self.assertEqual(app.return_secret_env(), os.environ['MY_SECRET_VARIABLE'])

if __name__ == '__main__':
    unittest.main()
