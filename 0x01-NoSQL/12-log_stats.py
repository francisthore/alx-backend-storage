#!/usr/bin/env python3
"""Script that writes stats about nginx logs"""
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx
    results = {}
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    total_logs = nginx_collection.count_documents({})
    for method in methods:
        results[method] = nginx_collection.count_documents(
            {'method': '{}'.format(method)}
            )
    get_path_status = nginx_collection.count_documents(
        {
            'method': 'GET',
            'path': '/status'
        }
    )
    print('{} logs'.format(total_logs))
    print('Methods:')
    for key, val in results.items():
        print('\tmethod {}: {}'.format(key, val))
    print('{} status check'.format(get_path_status))
