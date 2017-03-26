---
--- Example of table creation
---

-- Drop the table if it exists
IF OBJECT_ID('table_name') IS NOT NULL
  DROP TABLE table_name

-- Create a table with different variables. Not null variables must be always be filled, the rest
-- may have null values
CREATE TABLE table_name
(
     patient_id varchar(50) not null,
     size_row integer not null,
     size_col integer not null,
     array varbinary(max)
)

