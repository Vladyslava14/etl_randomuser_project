CREATE TABLE IF NOT EXISTS users (
    user_id UUID PRIMARY KEY,

    first_name VARCHAR(100),
    last_name VARCHAR(100),
    gender VARCHAR(10),

    date_of_birth DATE,
    age INTEGER,

    street_number INTEGER,
    street_name VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    postcode VARCHAR(20),

    latitude NUMERIC(9,6),
    longitude NUMERIC(9,6),

    email VARCHAR(255),
    phone VARCHAR(50),
    cell VARCHAR(50),
    nationality VARCHAR(10),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT*FROM users

TRUNCATE TABLE users; -- видалити insert таблиці

