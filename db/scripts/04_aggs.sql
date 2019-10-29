-- https://www.postgresql.org/docs/current/functions-aggregate.html
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
    col1
  , COUNT(col2)
  , MIN(col2)
  , MAX(col2)
  , AVG(col3)
  , SUM(col3)
  , ARRAY_AGG(col4)
FROM
  t
GROUP BY
  col1
;