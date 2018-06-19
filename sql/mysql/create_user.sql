-- Create a new SQL login user
-- Replace login name 'miguel' and password with your choice of user name/password
-- In version 8, the default authentification method is caching sha2
-- https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html 
CREATE USER IF NOT EXISTS 'miguel'@'localhost' IDENTIFIED BY 'miguel1234';
 
-- To create a new user with the legacy password method:
CREATE USER 'nativeuser'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'password';

-- To grant root priviledges
GRANT ALL PRIVILEGES ON *.* TO 'nativeuser'@'localhost'

