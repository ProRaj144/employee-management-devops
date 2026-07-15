REATE DATABASE IF NOT EXISTS employee_db;

USE employee_db;

CREATE TABLE IF NOT EXISTS employees (
	    id INT AUTO_INCREMENT PRIMARY KEY,
	    first_name VARCHAR(100) NOT NULL,
	    last_name VARCHAR(100) NOT NULL,
	    email VARCHAR(150) UNIQUE NOT NULL,
	    department VARCHAR(100),
	    designation VARCHAR(100),
	    salary DECIMAL(10,2),
	    photo_url VARCHAR(255),
	    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	        ON UPDATE CURRENT_TIMESTAMP
		);

		INSERT INTO employees
		(first_name,last_name,email,department,designation,salary)
		VALUES
		('John','Doe','john@example.com','IT','Developer',60000),
		('Alice','Smith','alice@example.com','HR','Manager',70000),
		('David','Brown','david@example.com','Finance','Analyst',65000);
