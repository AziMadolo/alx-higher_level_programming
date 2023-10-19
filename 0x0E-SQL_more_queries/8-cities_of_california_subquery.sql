-- Retrieves city IDs and names from the 'cities' table where state is California
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
