-- Retrieves the names of all tables within a specific database in my MySQL server.
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'your_database_name';





