-- Create a table users
-- id: integer, never null, auto increment and primary key
-- email: string(255), never null and unique
-- name: string(255)
-- country: enumeration of countries: US, CO and TN, never null, default US

CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
)