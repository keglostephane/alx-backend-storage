#!/usr/bin/env python3
"""nginx_stats_ip"""
from pymongo import MongoClient

client = MongoClient()
db = client.logs
nginx = db.nginx


def print_nginx_stats(nginx):
    """Prints some stats about Nginx logs stored in MongoDB"""
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


def print_top_ips(nginx):
    """Prints the top ips"""
    top_ips = nginx.aggregate([
        {'$group':
            {
                '_id': "$ip",
                'totalRequests': {'$sum': 1}
            }
         },
        {'$sort':
            {'totalRequests': -1}
         },
        {'$limit': 10},
    ])

    print("IPs:")
    for ip in top_ips:
        print("\t{}: {}".format(ip['_id'], ip['totalRequests']))


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    nginx = db.nginx

    print_nginx_stats(nginx)
    print_top_ips(nginx)
