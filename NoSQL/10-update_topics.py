#!/usr/bin/env python3
"""Module that updates a school document's topics by name."""


def update_topics(mongo_collection, name, topics):
    """Set the topics list for every document matching the given name."""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
