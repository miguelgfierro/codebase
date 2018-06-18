---
--- Example of table creation
---

USE my_database;

-- Drop the table if it exists
DROP TABLE IF EXISTS table_name;

CREATE TABLE table_name 
(
  id SMALLINT NOT NULL auto_increment,   
  recid int(11) NOT NULL DEFAULT '0',       
  filename VARCHAR(250)  NOT NULL DEFAULT '',     
  num int(11) NULL, 
  float_num FLOAT(8,6) NOT NULL DEFAULT '0',
  letter CHAR(1),
  input_date DATE,
   PRIMARY KEY  (id)
);

DESCRIBE table_name;

SELECT * FROM table_name;
