-- Select all entries equal to a value in a column
SELECT * FROM table_name WHERE column_name = value;

-- Select data in columns c1, c2 from a table
SELECT c1, c2 FROM t;

-- Select top N values of specific column names
SELECT TOP (5) column_name1, column_name2 FROM table_name;

-- Select the last entry equal to a value in a column ordered by other column 
SELECT TOP(1) * FROM table_name
WHERE column_name = value ORDER BY time_stamp DESC;

