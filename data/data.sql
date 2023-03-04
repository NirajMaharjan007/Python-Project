CREATE DATABASE IF NOT EXISTS my_database;
create table admins (
    id int(11) NOT NULL primary KEY,
    name varchar(255),
    password VARCHAR(255)
);
INSERT INTO admins
VALUES (1, "admin", "admin"),
    (2, "admin", "");
create table employees (
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
SELECT COUNT(emp_id)
FROM employees
WHERE admin_id = '2';