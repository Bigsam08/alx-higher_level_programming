-- Create database 'hbtn_0d_2'
-- Create user 'user_0d_2'
-- User password should be set to 'user_0d_2_pwd'
-- User 'user_0d_2' should have only SELECT privilege in db 'hbtn_0d_2'
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
