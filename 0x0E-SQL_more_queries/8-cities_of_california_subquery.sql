-- List all cities in California (avoiding JOIN)
SELECT cities.id, cities.name 
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;
