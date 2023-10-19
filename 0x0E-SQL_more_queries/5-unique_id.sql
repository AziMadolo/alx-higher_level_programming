-- Ensures table existence in the database with a unique constraint on id column
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE KEY unique_id (id)
);
