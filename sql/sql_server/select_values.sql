-- Select all entries equal to a value in a column
SELECT * FROM table_name WHERE column_name = value;

-- Select data in columns column_name1, column_name2 from a table
SELECT column_name1, column_name2 FROM table_name;

-- Select distinct rows from a table
SELECT DISTINCT column_name FROM table_name WHERE column_name = value;

-- Select top N values of specific column names
SELECT TOP (5) column_name1, column_name2 FROM table_name;

-- Select the last entry equal to a value in a column ordered by other column 
SELECT TOP(1) * FROM table_name
WHERE column_name = value ORDER BY time_stamp DESC;

-- Skip offset of rows and return the next n rows
SELECT column_name1, column_name2 FROM table_name 
ORDER BY column_name1 LIMIT n OFFSET offset;

-- Query rows using pattern matching %, _
SELECT column_name1, column_name2 FROM t1
WHERE column_name1 [NOT] LIKE pattern;

-- Query rows in a list
SELECT column_name1, column_name2 FROM table_name
WHERE column_name1 [NOT] IN value_list;

-- Query rows between two values
SELECT column_name1, column_name2 FROM table_name
WHERE column_name1 BETWEEN low AND high;

-- Check if values in a table is NULL or not
SELECT column_name1, column_name2 FROM table_name
WHERE column_name1 IS [NOT] NULL;