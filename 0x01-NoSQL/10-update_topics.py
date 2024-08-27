#!/usr/bin/env python3
"""Defines a function that updates on doc"""


def update_topics(mongo_collection, name, topics):
    """Updates topics of a school doc"""
    mongo_collection.update_one(
        {'name': name},
        {'$set': {
            'topics': topics
        }}
    )
