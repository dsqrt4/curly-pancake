-- create todos
-- depends: 

CREATE TABLE todos(
	id INT AUTO_INCREMENT PRIMARY KEY,
	title VARCHAR(255) NOT NULL,
	done BOOLEAN DEFAULT False
);
