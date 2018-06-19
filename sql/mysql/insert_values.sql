--
-- Example of values insertion in a table
--
USE my_database;

-- The primary key is an auto-increment value, there is no need to insert it
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

-- Load a csv file
LOAD DATA LOCAL INFILE '/Users/miguel/run3x/codebase/share/traj.csv'
INTO TABLE table_csv  
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(t, q0 , q1);

LOAD DATA INFILE '/Users/miguel/run3x/codebase/share/traj.csv' 
INTO TABLE table_csv;

SELECT * FROM table_csv;
