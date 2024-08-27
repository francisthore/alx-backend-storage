#!/usr/bin/env python3
"""Module that defines a function that inserts
a doc into a collection"""


def insert_school(mongo_collection, **kwargs):
    """Inserts one doc into a collection"""
    inserted_doc = mongo_collection.insert_one(kwargs)
    id = inserted_doc.inserted_id
    return id
