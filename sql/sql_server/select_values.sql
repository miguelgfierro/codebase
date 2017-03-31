-- Select the last entry of a column
SELECT TOP(1) * FROM table_name
WHERE column_name = ? ORDER BY time_stamp DESC;

-- Select top N values of a specific column names
SELECT TOP (5) column_name1, column_name2 FROM table_name;

-- Select all entries equal to a value in a column
SELECT * FROM table_name WHERE column_name = ?

-- Select values from different tables. Example: There are 2 tables, one has ProductID, ProductNameEnglish
-- and Price. The other table has ProductID and ProductNameSpanish. To select the price and the spanish
-- name:
SELECT t1.Price, t2.ProductNameSpanish FROM table_name1 AS t1
INNER JOIN table_name2 AS t2 ON t1.ProductID = t2.ProductID


