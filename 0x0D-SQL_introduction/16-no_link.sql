-- Lists all records of 'second_table' having a name value.
-- Records are ordered in descending order.
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
