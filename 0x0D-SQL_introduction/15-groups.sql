-- kist number of records
-- with same score in second_table
SELECT score AS "score",
COUNT(score) AS "number"
FROM second_table
GROUP BY score
ORDER BY number DESC;
