#!/usr/bin/env python3
"""list_collection_documents
"""


def list_all(mongo_collection):
    """Lists all documents in a collection.

    :param mongo_collection: a MongoDB collection
    :return: a list of all documents in the collection.
        an empty list if no document in the collection
    """
    return mongo_collection.find({})
