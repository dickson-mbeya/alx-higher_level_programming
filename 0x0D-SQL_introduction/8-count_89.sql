-- count 89
-- from first_table table
SELECT id,
    COUNT(id)
FROM first_table
HAVING COUNT(id) = 89;
