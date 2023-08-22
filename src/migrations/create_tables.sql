CREATE TABLE IF NOT EXISTS orders (
                id SERIAL PRIMARY KEY,
                created_date DATE NOT NULL DEFAULT CURRENT_DATE,
                updated_date DATE NOT NULL DEFAULT CURRENT_DATE,
                title VARCHAR(255) NOT NULL,
                total DECIMAL(10, 2) NOT NULL);

CREATE TABLE IF NOT EXISTS items (
                        id SERIAL PRIMARY KEY,
                        order_id INT REFERENCES orders(id),
                        name VARCHAR(255) NOT NULL,
                        price DECIMAL(10, 2) NOT NULL,
                        number INT NOT NULL);
