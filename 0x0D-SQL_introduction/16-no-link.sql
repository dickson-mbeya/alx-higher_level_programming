-- list all records of table second table
-- of the database hbtn_0c_0 in MySQL server
SELECT score AS "score", name AS "name",
FROM second_table
WHERE name!= NULL
GROUP BY score DESC;
