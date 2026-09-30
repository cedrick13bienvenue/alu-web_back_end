#!/usr/bin/env python3
"""Module for password hashing and validation."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return a salted, hashed version of the given password."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Return whether the given password matches the hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)
