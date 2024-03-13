-- Lists the number of records with the same score in 'second_table'.
-- Records are ordered in descending order.
SELECT score, COUNT(1) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
