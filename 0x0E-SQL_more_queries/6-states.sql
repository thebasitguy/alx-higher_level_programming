-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on my MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Uses a database
USE hbtn_0d_usa;
-- Creates a table
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
