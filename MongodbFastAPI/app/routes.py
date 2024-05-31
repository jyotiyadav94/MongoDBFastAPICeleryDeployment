'''



from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from fastapi import HTTPException
from fastapi import APIRouter, HTTPException
from MongoDB.mongo_connection import db


router = APIRouter()

'''
@router.get("/data")
async def read_root():
    return {"message": "Hello World"}
'''


@router.get("/data/")
async def read_root():
    """
    Get a list of all data.

    Returns:
        list: A list of employee records as JSON objects.
    """

    # Query the database to retrieve all employees
    employees = list(db.items.find({}))

    # If no employees are found, return an empty list
    if not employees:
        return []

    # Convert ObjectId to string for serialization (if needed)
    for employee in employees:
        employee["_id"] = str(employee["_id"])

    return employees
'''

