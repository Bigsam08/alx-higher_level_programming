-- Create db 'hbtn_0d_usa'
-- Create table 'cities' in db 'hbtn_0d_usa'
-- id INT unique, auto generated, not null, primary key
-- state_id INT not null, foreign key that references id of 'states' table
-- name VARCHAR(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id)
		REFERENCES hbtn_0d_usa.states(id)
);
