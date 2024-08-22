-- Creates a users table
-- that has some ENUM options
CREATE TABLE IF NOT EXISTS users (
  id INT auto_increment NOT NULL PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') DEFAULT 'US'
);
