-- Creates a view of students needing a meeting: score < 80 and no
-- recent last_meeting (none at all, or more than a month ago)
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH));
