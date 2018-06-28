-- Select all entries equal to a value in a column
SELECT * FROM table_name WHERE column_name = value


-- Select top N values of specific column names
SELECT column_name1, column_name2 FROM table_name ASC LIMIT 5;


-- Select top N rows ordered by a column
SELECT * FROM table_name ORDER BY column_name ASC LIMIT 5;


-- Select a random row
SELECT * FROM table_name LIMIT 1
OFFSET ABS(RANDOM()) % MAX((SELECT COUNT(*) FROM table_name), 1)
