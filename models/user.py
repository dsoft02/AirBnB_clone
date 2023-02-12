#!/usr/bin/python3
"""This module defines the User Class module for the AirBnB clone project"""
from models.base_model import BaseModel


class User(BaseModel):
    """Representation of a User

    Attributes:
        email (str): The email of the user.
        password (str): The user password.
        first_name (str): The user first name.
        last_name (str): The user last name.
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
