-- Drop the table if it exists
IF OBJECT_ID('table_name') IS NOT NULL
DROP TABLE table_name;

-- Create a table with different variables. Not null variables must be always be filled, the rest
-- may have null values
CREATE TABLE table_name
(
     patient_id varchar(50) NOT NULL PRIMARY KEY,
     size_row INT NOT NULL,
     size_col INT DEFAULT 0,
     array varbinary(max)
);

-- Add a new column to the table
ALTER TABLE t ADD column;

-- Drop column c from the table 
ALTER TABLE t DROP COLUMN c ;

