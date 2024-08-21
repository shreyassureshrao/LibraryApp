# Have a file named as "test_"...pytest will detect automatically and run the test
# To run test -> 
# a. [pip install pytest]
# b. [pytest --disable-warnings]  ---> will run the test and return pass or fail

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

# Because this file is in the same package, you can use relative imports to import the object app from the main module (main.py)
from .main import app

client = TestClient(app)

try:
    def test_read_main():
        response = client.get("/")
        assert response.status_code == 200

    def test_read_item():
        response = client.get("/books/1")
        assert response.status_code == 200
        assert response.json() == {
            "id": 1, 
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "isbn": "978-0-06-112008-4",
            "publishedDate": "1960-07-11",
            "price": 799

        }
       
# the errror_message provided by the user gets printed
except AssertionError as msg:
    print(msg)