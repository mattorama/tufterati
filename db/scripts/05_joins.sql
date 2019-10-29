-- https://www.postgresql.org/docs/11/queries-table-expressions.html#QUERIES-FROM
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
SELECT
    *
FROM
  t AS t1
  INNER JOIN t AS t2 USING (col1)
  LEFT OUTER JOIN t AS t3 ON t2.col3 = t3.col4
  CROSS JOIN t AS t4
;