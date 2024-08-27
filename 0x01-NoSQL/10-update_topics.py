#!/usr/bin/env python3
"""Defines a function that updates on doc"""
from typing import List

def update_topics(mongo_collection, name: str, topics: List[str]):
    """Updates topics of a school doc"""
    mongo_collection.update_many(
        {'name': name},
        {'$set': {
            'topics': topics
        }}
    )
