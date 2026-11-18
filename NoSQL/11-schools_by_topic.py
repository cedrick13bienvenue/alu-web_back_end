#!/usr/bin/env python3
"""Module that finds schools offering a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of school documents that teach the given topic."""
    return list(mongo_collection.find({"topics": topic}))
