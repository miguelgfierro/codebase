---
--- Example of values insertion in a table
---
USE my_database;

--- The primary key is an auto-increment value, there is no need to insert it
INSERT INTO table_name 
(
recid,
filename,
float_num,
letter,
input_date
)
VALUES 
(
77,
'miguel.csv',
3.14159,
'A',
'2017-04-12'
);

SELECT * FROM table_name;

