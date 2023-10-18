-- Displays records from the table second_table where the score is greater than or equal to 10.
-- The results are sorted in descending order based on the score.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
