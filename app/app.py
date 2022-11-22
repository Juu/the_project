"""This script is an example script"""
import os

def return_ok():
    return 'Ok'

def return_secret_env():
    return os.environ['MY_SECRET_VARIABLE']
