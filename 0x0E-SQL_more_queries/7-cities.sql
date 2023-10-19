-- Ensures database existence and sets it as active
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Creates a table with unique id, non-null state_id, non-null name, and foreign key reference to states table
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
);
