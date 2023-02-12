#!/usr/bin/python3
""" Amenity Class Module for the AirBnB clone project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity

    Attributes:
        name (str) : The name of the amenity
    """
    name = ""
