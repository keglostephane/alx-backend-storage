#!/usr/bin/env python3
"""students_storted_by_average"""


def top_students(mongo_collection):
    """Returns all students storted by average score.

    :paraam mongo_collection: a MongoDB collection
    :return: a list of top students sorted by average score
    :rtype: list of dict
    """
    return mongo_collection.aggregate([
        {"$project":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
         },
        {"$sort":
            {"averageScore": -1}
         }
    ])
