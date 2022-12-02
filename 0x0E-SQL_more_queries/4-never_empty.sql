-- creates the table id_not_null on your MySQL server
-- id_not_null description: id int with the default value 1, name VARCHAR(256)
-- The database will be passed as anargument of the mysql command

CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
