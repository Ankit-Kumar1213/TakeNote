from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from pymongo import MongoClient

app = FastAPI()

conn = MongoClient("mongodb+srv://iit2020259:Akiiita@cluster1.ehzqosf.mongodb.net")

