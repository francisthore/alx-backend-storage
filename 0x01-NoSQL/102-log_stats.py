#!/usr/bin/env python3
"""
Module to analyze and print log statistics from an nginx MongoDB collection.
"""
from pymongo import MongoClient


def log_stats():
    """
    Connects to the MongoDB server, retrieves log statistics from the 'nginx'
    collection, and prints a summary of request methods, path-specific stats,
    and the top 10 IP addresses by request count.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    total = logs_collection.count_documents({})

    get = logs_collection.count_documents({"method": "GET"})
    post = logs_collection.count_documents({"method": "POST"})
    put = logs_collection.count_documents({"method": "PUT"})
    patch = logs_collection.count_documents({"method": "PATCH"})
    delete = logs_collection.count_documents({"method": "DELETE"})

    path = logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
        )

    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")

    print("IPs:")
    sorted_ips = logs_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])
    for i, ip_info in enumerate(sorted_ips):
        if i == 10:
            break
        print(f"\t{ip_info.get('_id')}: {ip_info.get('count')}")


if __name__ == "__main__":
    log_stats()
