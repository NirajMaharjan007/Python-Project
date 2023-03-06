CREATE DATABASE IF NOT EXISTS my_database;

USE my_database;

create table
    admins (
        id int(11) NOT NULL primary KEY,
        name varchar(255),
        password VARCHAR(255)
    );

INSERT INTO admins VALUES (1, 'admin', 'admin'), (2, 'admin', '');

create table
    employees (
        emp_id int(11) NOT NULL primary KEY AUTO_INCREMENT,
        emp_name varchar(255),
        address varchar(255),
        email varchar(255),
        dob DATE,
        gender varchar(255),
        phone_no VARCHAR(255),
        admin_id int(11) NOT NULL,
        Foreign Key (admin_id) REFERENCES admins(id) ON DELETE CASCADE ON UPDATE CASCADE
    );

SELECT COUNT(emp_id) FROM employees WHERE admin_id = '2';

create table
    performance(
        emp_id int(11) NOT NULL,
        Foreign Key (emp_id) REFERENCES employees(emp_id) ON DELETE CASCADE ON UPDATE CASCADE,
        result int,
        attitude int,
        project_completed int,
        attenance int,
        performance_id int PRIMARY key AUTO_INCREMENT
    );

SELECT
    employees.emp_id,
    emp_name,
    performance.result,
    performance.attitude,
    performance.project_completed,
    performance.attenance
FROM employees
    LEFT JOIN performance ON employees.emp_id = performance.emp_id;