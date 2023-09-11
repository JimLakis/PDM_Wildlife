'''
Author: James Lakis

Start Date: Sep 11, 2023


'''

from fastapi.testclient import TestClient
from fastapi import status
#import httpx


# Relative import of app from main.py
from app import app


client = TestClient(app = app)


def test_index_response():
    response = client.get('/')
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message" : "Hello World!"}