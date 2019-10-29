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
SELECT
    col4
  , MIN(col3) AS min_col3 -- aggregate
FROM
  t
WHERE
  col3 < 9 -- condition
GROUP BY
  col4 -- aggregate
HAVING
  SUM(col1) > 4 -- aggregate condition
ORDER BY
  min_col3
LIMIT 1 -- max records
OFFSET 1 -- skip records
;