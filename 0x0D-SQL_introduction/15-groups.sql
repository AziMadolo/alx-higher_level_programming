-- Displays the count of records sharing the same score from the table second_table in the MySQL server.
-- The results are sorted in descending order based on the count.
SELECT score, COUNT(*) AS count
FROM second_table
GROUP BY score
ORDER BY count DESC;
