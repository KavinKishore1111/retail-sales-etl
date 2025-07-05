CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50)
);

CREATE TABLE sales(
    sale_id INT PRIMARY KEY,
    sale_date DATE NOT NULL,
     customer_id INT REFERENCES customers(customer_id) NOT NULL,
    product_id TEXT  NOT NULL,
    sale_amount NUMERIC  NOT NULL
)