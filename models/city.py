#!/usr/bin/python3
""" City Class Module for the AirBnB clone project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class is a representation of a city

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
