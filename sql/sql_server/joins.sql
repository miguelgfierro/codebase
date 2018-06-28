
-- INNER JOIN: Select values as the intersection of the two tables, i.e. rows they have common in table1 and table1
SELECT table1.column1, table2.column2
FROM table1 INNER JOIN table2
ON table1.common_field = table2.common_field;
-- Example:
SELECT TableA.firstName,TableA.lastName,TableB.age,TableB.Place
FROM TableA
INNER JOIN TableB
ON TableA.id = TableB.id2;
-- Result:
firstName       lastName       age  Place
..............................................
arun            prasanth        24  kerala
ann             antony          24  usa
sruthy          abc             25  ekm


-- LEFT JOIN: will give all selected rows in TableA, plus any common selected rows in TableB.
SELECT table1.column1, table2.column2...
FROM table1
LEFT JOIN table2
ON table1.common_field = table2.common_field;
-- Example:
SELECT TableA.firstName,TableA.lastName,TableB.age,TableB.Place
FROM TableA
LEFT JOIN TableB
ON TableA.id = TableB.id2;
-- Result:
firstName                   lastName                    age   Place
...............................................................................
arun                        prasanth                    24    kerala
ann                         antony                      24    usa
sruthy                      abc                         25    ekm
new                         abc                         NULL  NULL


-- RIGHT JOIN: will give all selected rows in TableB, plus any common selected rows in TableA.
SELECT table1.column1, table2.column2...
FROM table1
RIGHT JOIN table2
ON table1.common_field = table2.common_field;
-- Example:
SELECT TableA.firstName,TableA.lastName,TableB.age,TableB.Place
FROM TableA
RIGHT JOIN TableB
ON TableA.id = TableB.id2;
-- Result:
firstName                   lastName                    age     Place
...............................................................................
arun                        prasanth                    24     kerala
ann                         antony                      24     usa
sruthy                      abc                         25     ekm
NULL                        NULL                        24     chennai


-- FULL JOIN: It is same as union operation, it will return all selected values from both tables.
SELECT table1.column1, table2.column2...
FROM table1
FULL JOIN table2
ON table1.common_field = table2.common_field;
--Example:
SELECT TableA.firstName,TableA.lastName,TableB.age,TableB.Place
FROM TableA
FULL JOIN TableB
ON TableA.id = TableB.id2;
-- Result:
firstName                   lastName                    age    Place
...............................................................................
arun                        prasanth                    24    kerala
ann                         antony                      24    usa
sruthy                      abc                         25    ekm
new                         abc                         NULL  NULL
NULL                        NULL                        24    chennai
