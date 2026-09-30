#!/usr/bin/env python3
"""Module for filtering and logging personal data."""
import logging
import os
import re
from typing import List, Tuple

import mysql.connector


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str,
        separator: str) -> str:
    """Obfuscate the values of the given fields in a log message."""
    pattern = r'({})=[^{}]*'.format('|'.join(fields), separator)
    return re.sub(
        pattern, lambda m: '{}={}'.format(m.group(1), redaction), message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initialize the formatter with the fields to redact
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format a log record, redacting the configured PII fields
        """
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(
            self.fields, self.REDACTION, message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Return a logger configured to redact PII fields."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Return a connector to the personal data database."""
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")
    return mysql.connector.connect(
        user=username, password=password, host=host, database=db_name)


def main() -> None:
    """Retrieve all rows from the users table and log them, redacted."""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    field_names = [i[0] for i in cursor.description]
    logger = get_logger()
    for row in cursor:
        message = "".join(
            "{}={}; ".format(field, value)
            for field, value in zip(field_names, row))
        logger.info(message.strip())
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
