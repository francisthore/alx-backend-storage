#!/usr/bin/env python3
"""Module that defines a function that returns a list
of documents from a db collection"""

def list_all(mongo_collection):
    """Lists all documents in a db collection"""
    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
    return docs
