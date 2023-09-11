'''
Author: James Lakis

Start Date: Sep 11, 2023


'''

from fastapi.testclient import TestClient
from fastapi import status
import httpx


# Relative import of app from app.py
# Adding this package's path to the system path in order to perform relative import statements
import sys
my_package = r'C:\Users\Development\eclipse-workspace-PDM\PDM_Wildlife'
sys.path.append(my_package)

from app import app


client = TestClient(app = app)


def test_index_response():
    response = client.get('/')
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message" : "Hello World!"}