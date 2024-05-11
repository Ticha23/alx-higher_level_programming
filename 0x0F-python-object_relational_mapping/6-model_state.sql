-- Create database hbtn_0e_6_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;

-- Switch to the database hbtn_0e_6_usa
USE hbtn_0e_6_usa;

-- Drop the states table if it exists
DROP TABLE IF EXISTS states;

-- Create the states table
CREATE TABLE states (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(128) NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

