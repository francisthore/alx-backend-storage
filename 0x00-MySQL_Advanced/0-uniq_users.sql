-- Creates a table that stores users
-- The user.email is a unique column 

CREATE TABLE IF NOT EXISTS users (
  id INT auto_increment NOT NULL PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);
