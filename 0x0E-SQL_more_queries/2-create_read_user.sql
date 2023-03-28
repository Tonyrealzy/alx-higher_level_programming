-- script that creates the database hbtn_0d_2 and the user user_0d_2

CREATE IF NOT EXISTS user_0d_2@localhost
IDENTIFIED WITH authentication_plugin BY user_0d_2;

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

GRANT SELECT on *.*
TO user_0d_2@localhost;
