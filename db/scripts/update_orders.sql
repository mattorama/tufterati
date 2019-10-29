select version();

create TEMPORARY TABLE Orders AS (
  SELECT *
    FROM (
      VALUES 
          (1, 10)
        , (2, 11)
    ) dummy_name (id, merchant_id)
)
;
select * from Orders;

create TEMPORARY table  Merchants AS (
  SELECT *
  FROM (
    VALUES
        (10, 'a')
      , (11, 'b')
    ) dummy_name (id, name)
)
;
select * from Merchants;

alter table Orders add merchant_name text;
select * from Orders;

UPDATE Orders
SET merchant_name = Merchants.name
FROM Merchants
WHERE merchant_id = Merchants.id;

select * from Orders;