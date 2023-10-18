-- Retrieves records from the table second_table where the name is not empty.
-- The results are sorted in descending order based on the score.
SELECT score, name
FROM second_table
WHERE LENGTH(name) > 0
ORDER BY score DESC;
