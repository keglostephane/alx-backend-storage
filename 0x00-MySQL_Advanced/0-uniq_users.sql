-- Create a table user
-- id: integer, never null, auto increment and primary key
-- email: string(255), never null and unique
-- name: string(255)

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
)