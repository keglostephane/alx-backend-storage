#!/usr/bin/env python3
"""nginx_stats"""
from pymongo import MongoClient


def print_nginx_stats():
    """Prints some stats about Nginx logs stored in MongoDB"""
    client = MongoClient()
    db = client.logs
    nginx = db.nginx
    results = f"""{nginx.count_documents({})} logs
Methods:
\tmethod GET: {nginx.count_documents({"method": "GET"})}
\tmethod POST: {nginx.count_documents({"method": "POST"})}
\tmethod PUT: {nginx.count_documents({"method": "PUT"})}
\tmethod PATCH: {nginx.count_documents({"method": "PATCH"})}
\tmethod DELETE: {nginx.count_documents({"method": "DELETE"})}
{nginx.count_documents({"path": "/status"})} status check
"""
    print(results, end="")


if __name__ == "__main__":
    print_nginx_stats()
