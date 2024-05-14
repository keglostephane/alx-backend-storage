#!/usr/bin/env python3
"""list_school_with_specific_topics
"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic.

    :param mongo_collection: a mongoDB collection
    :param topic: topics searched
    :type topic: str
    :return: the list of school having `topic`
    :rtype: list
    """
    return mongo_collection.find({'topics': topic})
