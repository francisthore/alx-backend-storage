#!/usr/bin/env python3
"""Defines a funtion that finds
docs by topic"""


def schools_by_topic(mongo_collection, topic: str):
    """Returns a list of schools having a specific topic"""
    docs_arr = []
    docs = mongo_collection.find(
        {
            'topics': topic
        }
    )
    for doc in docs:
        docs_arr.append(doc)
    return docs_arr
