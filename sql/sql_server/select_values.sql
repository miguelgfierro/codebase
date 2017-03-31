-- Select the last entry of a column
SELECT TOP(1) * FROM table_name
WHERE column_name = ? ORDER BY time_stamp DESC;

-- Select top N values of a specific column names
SELECT TOP (5) column_name1, column_name2 FROM table_name;

