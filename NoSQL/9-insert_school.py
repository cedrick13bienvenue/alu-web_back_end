#!/usr/bin/env python3
"""Module that inserts a new document into a MongoDB collection."""


def insert_school(mongo_collection, **kwargs):
    """Insert a document built from kwargs and return its new _id."""
    return mongo_collection.insert_one(kwargs).inserted_id
