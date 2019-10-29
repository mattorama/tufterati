SELECT VERSION();

-- https://modern-sql.com/feature/values

SELECT *
FROM (
  VALUES 
    (1, 2)
    , (3, 4)
  ) required_table_name (col1, col2)
;

WITH t AS (
  SELECT *
    FROM (
      VALUES 
        (1, 2)
        , (3, 4)
    ) required_table_name (col1, col2)
)
SELECT
 *
FROM
 t
;