-- Combine rows from two queries
SELECT c1, c2 FROM t1
UNION [ALL]
SELECT c1, c2 FROM t2;

-- Return the intersection of two queries
SELECT c1, c2 FROM t1
INTERSECT
SELECT c1, c2 FROM t2;

-- Subtract a result set from another result set
SELECT c1, c2 FROM t1
MINUS
SELECT c1, c2 FROM t2;

