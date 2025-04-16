CREATE DATABASE farmers_market;
USE farmers_market;

-- Create tables
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

-- Insert all vendors (10 total)
INSERT INTO Vendors (name, phone, stall_number) VALUES
('Green Farms', '555-1234', 1),
('Sunny Orchards', '555-5678', 2),
('Fresh Fields', '555-9012', 3),
('Blooming Meadows', '555-3456', 4),
('Harvest Haven', '555-7890', 5),
('Golden Acres', '555-2345', 6),
('River Bend Farms', '555-6789', 7),
('Meadow Mist', '555-0123', 8),
('Sunny Hills', '555-4567', 9),
('Evergreen Produce', '555-8901', 10);

-- Insert all products (20 total)
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
(5, 'Onions', 'Vegetable', 1.20, 150),
(6, 'Peaches', 'Fruit', 3.50, 90),
(6, 'Zucchini', 'Vegetable', 1.80, 60),
(7, 'Grapes', 'Fruit', 4.20, 50),
(7, 'Eggplant', 'Vegetable', 2.30, 40),
(8, 'Raspberries', 'Fruit', 5.50, 20),
(8, 'Broccoli', 'Vegetable', 2.00, 70),
(9, 'Pears', 'Fruit', 3.00, 80),
(9, 'Spinach', 'Vegetable', 1.50, 100),
(10, 'Cherries', 'Fruit', 6.00, 30),
(10, 'Cauliflower', 'Vegetable', 2.50, 50);

-- Insert all customers (15 total)
INSERT INTO Customers (name, email, loyalty_points) VALUES
('Jane Doe', 'jane@example.com', 10),
('John Smith', 'john@example.com', 5),
('Alice Johnson', 'alice@example.com', 15),
('Bob Wilson', 'bob@example.com', 8),
('Emma Davis', 'emma@example.com', 20),
('Michael Brown', 'michael@example.com', 12),
('Sarah Miller', 'sarah@example.com', 18),
('Olivia Taylor', 'olivia@example.com', 25),
('James Anderson', 'james@example.com', 14),
('Sophia Martinez', 'sophia@example.com', 30),
('Liam Harris', 'liam@example.com', 9),
('Ava Clark', 'ava@example.com', 22),
('Noah Lewis', 'noah@example.com', 16),
('Isabella Walker', 'isabella@example.com', 28),
('Mason Allen', 'mason@example.com', 11);

-- Insert all sales (20 total)
INSERT INTO Sales (product_id, quantity, sale_date, total) VALUES
(1, 5, '2025-04-10', 12.50),   -- Apples
(2, 3, '2025-04-11', 4.50),    -- Carrots
(3, 2, '2025-04-12', 6.00),    -- Oranges
(4, 4, '2025-04-12', 8.00),    -- Lemons
(5, 3, '2025-04-13', 6.60),    -- Tomatoes
(6, 2, '2025-04-13', 3.60),    -- Cucumbers
(7, 1, '2025-04-14', 4.00),    -- Strawberries
(8, 2, '2025-04-14', 10.00),   -- Blueberries
(9, 5, '2025-04-14', 5.00),    -- Potatoes
(10, 3, '2025-04-14', 3.60),   -- Onions
(11, 3, '2025-04-15', 10.50),  -- Peaches
(12, 4, '2025-04-15', 7.20),   -- Zucchini
(13, 2, '2025-04-16', 8.40),   -- Grapes
(14, 5, '2025-04-16', 11.50),  -- Eggplant
(15, 1, '2025-04-17', 5.50),   -- Raspberries
(16, 3, '2025-04-17', 6.00),   -- Broccoli
(17, 2, '2025-04-18', 6.00),   -- Pears
(18, 6, '2025-04-18', 9.00),   -- Spinach
(19, 1, '2025-04-19', 6.00),   -- Cherries
(20, 2, '2025-04-19', 5.00);   -- Cauliflower
