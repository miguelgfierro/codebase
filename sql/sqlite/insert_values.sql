-- Insert values in a table
INSERT INTO table_name 
(
id,
recid,
filename,
float_num,
letter,
input_date
)
VALUES 
(
0,
77,
'miguel.csv',
3.14159,
'A',
'2017-04-12'
);

SELECT * FROM table_name;

-- Load csv into table_csv
.mode csv
.import '/Users/miguel/run3x/codebase/share/traj.csv' table_csv
SELECT * FROM table_csv;



