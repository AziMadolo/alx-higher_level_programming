-- Ensures database existence and sets it as active
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Creates a table with unique id, non-null name, and auto-incrementing primary key
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
