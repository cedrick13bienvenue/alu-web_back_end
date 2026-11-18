# NoSQL

## Description
This project covers NoSQL fundamentals with MongoDB: shell scripts for
basic CRUD operations, and Python functions using PyMongo for the same
operations plus an aggregate stats script over real Nginx access logs.

## Resources
- [NoSQL Databases Explained](https://www.mongodb.com/nosql-explained)
- [MongoDB with Python Crash Course](https://www.freecodecamp.org/news/mongodb-with-python-crash-course-tutorial-for-beginners/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [mongo Shell Methods](https://docs.mongodb.com/manual/reference/method/)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- What NoSQL means, and the difference between SQL and NoSQL
- What ACID is
- What a document storage is, and the different NoSQL types
- The benefits of a NoSQL database
- How to query, insert, update, and delete information in a NoSQL database
- How to use MongoDB

## Requirements
### MongoDB command files
- Interpreted on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All files end with a new line
- The first line of all files is a comment: `// my comment`

### Python scripts
- Interpreted on Ubuntu 18.04 LTS using `python3` (version 3.7) and PyMongo (version 3.10)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style (version 2.5.*)
- All modules and functions are documented with real, explanatory docstrings
- No code runs on import - guarded by `if __name__ == "__main__":`

## Setup
```
service mongod start
pip3 install -r requirements.txt
```

## Tasks
| File | Description |
| --- | --- |
| `0-list_databases` | Lists all databases |
| `1-use_or_create_database` | Switches to (or creates) `my_db` |
| `2-insert` | Inserts a document into the `school` collection |
| `3-all` | Lists all documents in `school` |
| `4-match` | Finds documents with `name = "ALX"` |
| `5-count` | Counts documents in `school` |
| `6-update` | Adds an `address` to every `ALX` document |
| `7-delete` | Deletes every `ALX` document |
| `8-all.py` | `list_all` - lists every document in a collection |
| `9-insert_school.py` | `insert_school` - inserts a document from kwargs |
| `10-update_topics.py` | `update_topics` - sets a school's topics by name |
| `11-schools_by_topic.py` | `schools_by_topic` - finds schools teaching a given topic |
| `12-log_stats.py` | Prints Nginx log stats (total, by method, `/status` checks) from `logs.nginx` |

## Usage
```
cat 0-list_databases | mongo
cat 2-insert | mongo my_db
python3 12-log_stats.py
```

## Note on task 12
Tested against the real `dump.zip` log sample (94778 documents) restored
with `mongorestore`; output matches the task's example exactly.
