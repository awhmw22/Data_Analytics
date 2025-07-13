CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price NUMERIC(10,2) NOT NULL,
    cost NUMERIC(10,2) NOT NULL,
    supplier_id INT,
    CONSTRAINT chk_price_positive CHECK (price >= 0),
    CONSTRAINT chk_cost_positive CHECK (cost >= 0)
);

CREATE TABLE Suppliers (
    supplier_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(100)
);

CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    gender VARCHAR(10),
    location VARCHAR(100),
    signup_date DATE
);

CREATE TABLE Stores (
    store_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100),
    size VARCHAR(50)
);

CREATE TABLE Sales (
    sale_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    customer_id INT,
    date TIMESTAMP NOT NULL,
    quantity INT NOT NULL,
    store_id INT,
    channel VARCHAR(50), -- e.g., 'online', 'in-store'
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES Products(product_id),
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    CONSTRAINT fk_store FOREIGN KEY (store_id) REFERENCES Stores(store_id),
    CONSTRAINT chk_quantity_positive CHECK (quantity > 0)
);

CREATE TABLE Inventory (
    product_id INT NOT NULL,
    store_id INT NOT NULL,
    stock_level INT NOT NULL,
    last_restock_date DATE,
    PRIMARY KEY (product_id, store_id),
    CONSTRAINT fk_inv_product FOREIGN KEY (product_id) REFERENCES Products(product_id),
    CONSTRAINT fk_inv_store FOREIGN KEY (store_id) REFERENCES Stores(store_id),
    CONSTRAINT chk_stock_nonneg CHECK (stock_level >= 0)
);

ALTER TABLE Products
ADD CONSTRAINT fk_supplier FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id);
