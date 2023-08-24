CREATE TABLE IF NOT EXISTS orders (
                id SERIAL PRIMARY KEY,
                created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                title VARCHAR(255) NOT NULL,
                total DECIMAL(10, 2) NOT NULL DEFAULT 0.00);

CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    order_id INT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    number INT NOT NULL
);
