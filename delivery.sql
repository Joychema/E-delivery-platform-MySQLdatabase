-- create an e-delivery, e-commerce platform database schema
CREATE DATABASE deliverdb;

use deliverdb;                  

-- Table 1: Vendors
-- This table stores information about the businesses selling products.
CREATE TABLE Vendors(
	vendorID INT PRIMARY KEY,
    vendorname VARCHAR(100) NOT NULL,
    location VARCHAR(50)
    );
    
-- Table 2: Customers
-- This table stores information about the customers.
CREATE TABLE customers(
	customerID INT PRIMARY KEY,
    customername VARCHAR(100) not NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    address VARCHAR(255)
    );

-- Table 3: Drivers
-- This table stores information about the delivery drivers.
CREATE TABLE drivers(
	driverID INT PRIMARY KEY,
    drivername VARCHAR(100) NOT NULL,
    phonenumber VARCHAR(20) UNIQUE
    );
    
-- Table 4: Products
-- This table stores information about the products for sale.
-- It links to the Vendors table.
CREATE TABLE products(
	productID INT PRIMARY KEY,
    productname VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) not NULL,
    vendorID INT,
    FOREIGN KEY(vendorID) references Vendors(vendorID)
    );
    
-- Table 5: Orders
-- This table stores the main order details.
-- It links to the Customers and Drivers tables.
CREATE TABLE orders(
	orderID INT PRIMARY KEY,
    OrderDate DATE NOT NULL,
    Status VARCHAR(50),
    customerID INT,
    driverID INT,
    FOREIGN KEY(customerID) REFERENCES customers(customerID),
    FOREIGN KEY(driverID) REFERENCES drivers(driverID)
    );
    
-- Table 6: OrderItems
-- This is the linking table for the many-to-many relationship
-- between Orders and Products.
CREATE TABLE OrderItems (
    ItemID INT PRIMARY KEY,
    orderID INT,
    productID INT,
    Quantity INT NOT NULL,
    FOREIGN KEY (orderID) REFERENCES orders(orderID),
    FOREIGN KEY (productID) REFERENCES products(productID)
);

-- Insert sample data into the tables
INSERT INTO Vendors (VendorID, VendorName, Location)
VALUES 
(1, 'Strikas FC', 'Strikaland'),
(2, 'Invincible United', 'Invincible City'),
(3, 'FC All Stars', 'Madrid');

INSERT INTO Customers (CustomerID, CustomerName, Email, Address)
VALUES
(101, 'Shakes', 'shakes@strikas.com', '10 Main Street, Strikaland'),
(102, 'El Matador', 'matador@strikas.com', '7 City Avenue, Invincible City'),
(103, 'Cool Joe', 'cooljoe@allstars.com', '24 Downtown Road, Madrid');

INSERT INTO Drivers (DriverID, DriverName, PhoneNumber)
VALUES
(201, 'Skarra', '555-1234'),
(202, 'Dancing Rasta', '555-5678'),
(203, 'Twisting Tiger', '555-9012');

INSERT INTO Products (ProductID, ProductName, Price, VendorID)
VALUES
(1, 'Strikas FC Jersey', 49.99, 1),
(2, 'Invincible United Scarf', 15.00, 2),
(3, 'Strika Boot - Mach X', 89.99, 1),
(4, 'Official Strikas Football', 30.50, 1),
(5, 'FC All Stars Jersey', 49.99, 3);

INSERT INTO Orders (OrderID, CustomerID, DriverID, OrderDate, Status)
VALUES
(1001, 101, 201, '2025-09-24', 'Shipped'),
(1002, 102, 203, '2025-09-23', 'Delivered'),
(1003, 103, 202, '2025-09-24', 'Pending');

INSERT INTO OrderItems (ItemID, OrderID, ProductID, Quantity)
VALUES
(501, 1001, 1, 1),  -- Shakes orders a Strikas FC Jersey
(502, 1001, 4, 1),  -- Shakes also orders an Official Strikas Football
(503, 1002, 2, 1),  -- El Matador orders an Invincible United Scarf
(504, 1003, 5, 1);  -- Cool Joe orders an FC All Stars Jersey