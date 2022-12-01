-- creates a table called first_table in the current database in your Mysql server
-- The database name will be passed as an argument of the Mysql command
-- first_table description:
-- 		id INT
--		name VARCHAR(256)
-- the database will be passed as an argument of the mysql command
-- if the table first_table already exist, your script should not fail

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
	);
