CREATE DATABASE farmers_market;
USE farmers_market;

CREATE TABLE Vendors (
    vendor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    stall_number INT UNIQUE
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    vendor_id INT,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    FOREIGN KEY (vendor_id) REFERENCES Vendors(vendor_id)
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    loyalty_points INT DEFAULT 0
);

CREATE TABLE Sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    quantity INT NOT NULL,
    sale_date DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Insert more vendors
INSERT INTO Vendors (name, phone, stall_number) VALUES
('Green Farms', '555-1234', 1),
('Sunny Orchards', '555-5678', 2),
('Fresh Fields', '555-9012', 3),
('Blooming Meadows', '555-3456', 4),
('Harvest Haven', '555-7890', 5);

-- Insert more products
INSERT INTO Products (vendor_id, name, category, price, stock) VALUES
(1, 'Apples', 'Fruit', 2.50, 100),
(1, 'Carrots', 'Vegetable', 1.50, 50),
(2, 'Oranges', 'Fruit', 3.00, 80),
(2, 'Lemons', 'Fruit', 2.00, 60),
(3, 'Tomatoes', 'Vegetable', 2.20, 70),
(3, 'Cucumbers', 'Vegetable', 1.80, 40),
(4, 'Strawberries', 'Fruit', 4.00, 30),
(4, 'Blueberries', 'Fruit', 5.00, 25),
(5, 'Potatoes', 'Vegetable', 1.00, 200),
(5, 'Onions', 'Vegetable', 1.20, 150);

-- Insert more customers
INSERT INTO Customers (name, email, loyalty_points) VALUES
('Jane Doe', 'jane@example.com', 10),
('John Smith', 'john@example.com', 5),
('Alice Johnson', 'alice@example.com', 15),
('Bob Wilson', 'bob@example.com', 8),
('Emma Davis', 'emma@example.com', 20),
('Michael Brown', 'michael@example.com', 12),
('Sarah Miller', 'sarah@example.com', 18);

-- Insert more sales
INSERT INTO Sales (product_id, quantity, sale_date, total) VALUES
(1, 5, '2025-04-10', 12.50),
(2, 3, '2025-04-11', 4.50),
(3, 2, '2025-04-12', 6.00),
(4, 4, '2025-04-12', 8.00),
(5, 3, '2025-04-13', 6.60),
(6, 2, '2025-04-13', 3.60),
(7, 1, '2025-04-14', 4.00),
(8, 2, '2025-04-14', 10.00),
(9, 5, '2025-04-14', 5.00),
(10, 3, '2025-04-14', 3.60);
