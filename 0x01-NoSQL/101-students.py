#!/usr/bin/env python3
"""
    Module that defines a function that calculate avg
    score for students and sort them
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by their average score in descending order.
    Each document in the result includes an 'averageScore' field.
    """
    pipeline = [
        {
            "$addFields": {
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
