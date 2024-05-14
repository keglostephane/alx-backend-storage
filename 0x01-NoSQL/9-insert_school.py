#!/usr/bin/env python3
"""insert_document_on_collection
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document based on keyword arguments.

    :param mongo_collection: a MongoDB collection
    :param kwargs: keywords arguments
    :return: the new _id of the document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
