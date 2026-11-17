# MySQL advanced

## Description
This project covers more advanced MySQL features: constraints, triggers,
stored procedures and functions, views, and indexes for query
optimization.

## Resources
- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.datadoghq.com/blog/mysql-database-performance-optimization-tips/)
- [Stored Procedure](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
- [Triggers](https://dev.mysql.com/doc/refman/5.7/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/5.7/en/views.html)

## Learning Objectives
By the end of this project, you should be able to explain, without Google:
- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## Requirements
- All files executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- All files end with a new line
- Every SQL query has a comment just above it
- Every file starts with a comment describing the task
- All SQL keywords are in uppercase (`SELECT`, `WHERE`, ...)

## Setup
```
service mysql start
cat <file>.sql | mysql -uroot -p holberton
```

## Tasks
| File | Description |
| --- | --- |
| `0-uniq_users.sql` | `users` table with a unique email |
| `1-country_users.sql` | `users` table with a `country` enum (default `US`) |
| `2-fans.sql` | Ranks band origins by total fan count |
| `3-glam_rock.sql` | Lists Glam rock bands by longevity |
| `4-store.sql` | Trigger: decreases item quantity on new orders |
| `5-valid_email.sql` | Trigger: resets `valid_email` only when the email changes |
| `6-bonus.sql` | `AddBonus` stored procedure |
| `7-average_score.sql` | `ComputeAverageScoreForUser` stored procedure |
| `8-index_my_names.sql` | Index on the first letter of `names.name` |
| `9-index_name_score.sql` | Composite index on the first letter of `name` and `score` |
| `10-div.sql` | `SafeDiv` function, dividing without ever erroring on zero |
| `11-need_meeting.sql` | `need_meeting` view |

## Note on tasks 2, 3, 8, 9
These tasks require importing the `metal_bands.sql` and `names.sql` table
dumps referenced in the project page. The queries themselves are
data-independent and were verified locally against small synthetic
tables with the same columns and semantics (including the `split = 0`
"still active" case for task 3).
