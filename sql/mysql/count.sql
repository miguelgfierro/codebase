-- Count total number of rows in a table
SELECT COUNT(*) FROM my_database.table_name;

-- Count the number of non null records in a column
SELECT COUNT(column_name) FROM my_database.table_name;

-- Count the number of distinct records in a column
SELECT COUNT(DISTINCT column_name) FROM my_database.table_name;
