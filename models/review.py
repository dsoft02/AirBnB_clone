#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class to store review information

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The review message.
    """
    place_id = ""
    user_id = ""
    text = ""
