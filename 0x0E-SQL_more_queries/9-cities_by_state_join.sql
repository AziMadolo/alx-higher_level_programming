-- Retrieves city IDs, names, and their respective state names
SELECT cities.id AS city_id, cities.name AS city_name, states.name AS state_name
FROM cities
LEFT JOIN states ON states.id = cities.state_id
ORDER BY cities.id;
