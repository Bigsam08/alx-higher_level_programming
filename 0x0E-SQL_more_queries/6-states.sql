-- Create database 'hbtn_0d_usa'
-- Create table 'states' in db 'hbtn_0d_usa'
-- id INT unique auto-generated not null and primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
