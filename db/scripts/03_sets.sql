-- https://www.postgresql.org/docs/current/sql-select.html
WITH t AS (
  SELECT *
    FROM (
      VALUES 
          (1, 2, 5, 6)
        , (3, 4, 6, 6)
        , (5, 2, 8, 7)
        , (1, 4, 9, 7)
        , (3, 2, 7, 8)
        , (5, 4, 8, 8)
    ) required_table_name (col1, col2, col3, col4)
)
SELECT * FROM t WHERE col1 < 2
UNION ALL
SELECT * FROM t WHERE col2 > 2
EXCEPT ALL
SELECT * FROM t WHERE col4 = 6
INTERSECT ALL
SELECT * FROM t WHERE col3 = 9
;