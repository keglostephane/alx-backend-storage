#!/usr/bin/env python3
"""modify_topics_documents_collection
"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a `school` document based on name.

    :param mongo_collection: a MongoDB collection
    :param name: school name to update
    :param topics: the list of topics in the school
    """
    mongo_collection.update_one({'name': name},
                                {'$set': {'topics': topics}})
