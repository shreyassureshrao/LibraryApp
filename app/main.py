# Code to demonstrate RESTful API based application - with the data stored in JSON file
# Demonstrated for GET, GET ID, POST, PUT AND DELETE HTTP Methods
# URL to run -> http://localhost:8000/docs which opens the Swagger API documentation
# Run Uvicorn - uvicorn main:app --reload

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    isbn:str
    publishedDate:str
    price: int


import os

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'book.json')

with open(filename,'r') as f:
    book = json.load(f)['book']
    

@app.get('/')
def getAllBooks():
    return book


@app.get('/books/{b_id}', status_code=200)
def get_book(b_id: int):
    bookObj = [b for b in book if b['id'] == b_id]
    return bookObj[0] if len(bookObj) > 0 else {}
