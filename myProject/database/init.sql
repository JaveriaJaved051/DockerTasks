-- Create a simple table for testing purposes
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- Insert test data
INSERT INTO users (name, email) VALUES
('John Doe', 'john.doe@example.com'),
('Jane Doe', 'jane.doe@example.com');
