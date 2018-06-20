-- Drop the table if it exists
DROP TABLE IF EXISTS table_name;

-- Create a table
CREATE TABLE table_name 
(
  id SMALLINT NOT NULL PRIMARY KEY,   
  recid INT(11) NOT NULL DEFAULT '0',       
  filename VARCHAR(250)  NOT NULL DEFAULT '',     
  num INT(11) NULL, 
  float_num FLOAT(8,6) NOT NULL DEFAULT '0',
  letter CHAR(1),
  input_date DATE
 );

-- Show information about the table
PRAGMA table_info([table_name]);

-- Select all table
SELECT * FROM table_name;

