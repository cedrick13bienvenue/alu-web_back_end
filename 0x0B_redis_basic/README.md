# Redis basic

## Description
This project builds a small `Cache` class on top of Redis: storing and
retrieving typed data, counting how many times a method is called, and
recording the full input/output history of every call so it can be
replayed later.

## Resources
- [Redis commands](https://redis.io/commands)
- [Redis python client](https://redis-py.readthedocs.io/en/stable/)
- [How to Use Redis With Python](https://realpython.com/python-redis/)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- How to use Redis for basic operations
- How to use Redis as a simple cache

## Requirements
- All files interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/env python3`
- Code follows the `pycodestyle` style (version 2.5)
- All modules, classes, and functions are documented with real, explanatory docstrings
- All functions and coroutines are type-annotated

## Setup
```
sudo apt-get -y install redis-server
pip3 install redis
sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
service redis-server start
```
