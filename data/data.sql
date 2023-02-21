-- Active: 1657020369972@@127.0.0.1@3306

CREATE DATABASE IF NOT EXISTS my_database;

create table
    admins (
        id int(11) NOT NULL primary KEY,
        name varchar(255),
        password VARCHAR(255)
    );

INSERT INTO admins VALUES(1,"admin","admin");

create table
    employees (
        emp_id int(11) NOT NULL primary KEY AUTO_INCREMENT,
        emp_name varchar(255),
        address varchar(255),
        email varchar(255),
        dob VARCHAR(255),
        gender varchar(255),
        phone_no int(11),
        admin_id int(11) NOT NULL,
        Foreign Key (admin_id) REFERENCES admins(id)
    );