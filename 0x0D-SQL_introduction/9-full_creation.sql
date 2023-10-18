-- Creates a table named second_table with columns id (integer), name (string, maximum length 256), and score (integer) in the MySQL server, ensuring it's created if not already present.
CREATE TABLE IF NOT EXISTS second_table (
id INT,
name VARCHAR(256),
score INT
);

-- Inserts multiple records into the second_table in the MySQL server.
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);





