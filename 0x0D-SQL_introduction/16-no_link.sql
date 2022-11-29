-- list all records
-- except NULL
SELECT score AS "score", name AS "name"
FROM second_table
WHERE name != NULL
ORDER BY score DESC;
