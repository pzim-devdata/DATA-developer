-- 1 = sales
-- 2 = production
-- Désactiver temporairement les contraintes pr éviter les pb
-- SET FOREIGN_KEY_CHECKS = 0 ;
-- https://stackoverflow.com/questions/1905470/cannot-delete-or-update-a-parent-row-a-foreign-key-constraint-fails

-- CREATE SCHEMA

-- DROP SCHEMA IF EXISTS ZARA ;
CREATE SCHEMA ZARA ;
USE ZARA ;


-- CREATE TABLES

-- The categories table stores the bike’s categories such as children bicycles, comfort bicycles, and electric bikes.

CREATE TABLE categories2 (
	category_id INT AUTO_INCREMENT  PRIMARY KEY,
	category_name VARCHAR (255) NOT NULL
    
    
);

-- The brands table stores the brand’s information of bikes (caaracteristiques, particularités des vélos), for example, Electra, Haro, and Heller

CREATE TABLE brands2 (
	brand_id INT AUTO_INCREMENT  PRIMARY KEY,
	brand_name VARCHAR (255) NOT NULL
    
);

-- The products table stores the product’s information such as name, brand, category, model year, and list price.
-- Each product belongs to a brand specified by the brand_id column. Hence, a brand may have zero or many products.
-- Each product also belongs a category specified by the category_id column. Also, each category may have zero or many products.

CREATE TABLE products2 (
	product_id INT AUTO_INCREMENT  PRIMARY KEY,
	product_name VARCHAR (255) NOT NULL,
	brand_id INT NOT NULL,
	category_id INT NOT NULL,
	model_year SMALLINT NOT NULL,
	list_price DECIMAL (10, 2) NOT NULL
 	
);

-- The production.stocks table stores the inventory information i.e. the quantity of a particular product in a specific store.

CREATE TABLE stocks2 (
	store_id INT,
	product_id INT,
	quantity INT
 	
);

CREATE TABLE customers1 (
	customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR (45) NOT NULL,
    last_name VARCHAR (45) NOT NULL,
    phone VARCHAR(25),
    email VARCHAR (45) NOT NULL,
    street VARCHAR (45) NOT NULL,
    city VARCHAR (45) NOT NULL,
    state VARCHAR (45) NOT NULL,
    zip_code INT (5) NOT NULL
);

CREATE TABLE staffs1 (
	staff_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR (45) NOT NULL,
    last_name VARCHAR (45) NOT NULL,
    phone VARCHAR(25),
    email VARCHAR (45) NOT NULL,
    active ENUM ('0','1') NOT NULL,
    store_id INT,
    manager_id INT
);
    
CREATE TABLE orders1 (
	order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_status ENUM('0', '1', '2', '3', '4') NOT NULL,
    order_date DATETIME DEFAULT NOW() NOT NULL,
    required_date DATETIME,
    shipped_date DATETIME,
    store_id INT NOT NULL,
    staff_id INT NOT NULL    
);

CREATE TABLE stores1 (
	store_id INT AUTO_INCREMENT PRIMARY KEY,
    store_name VARCHAR (45) NOT NULL,
    phone VARCHAR (25),
    email VARCHAR (45) NOT NULL,
    street VARCHAR (45) NOT NULL,
    city VARCHAR (45) NOT NULL,
    state VARCHAR (45) NOT NULL,
    zip_code INT (5) NOT NULL    
);

CREATE TABLE order_items1 (
	item_id INT NOT NULL,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    list_price DECIMAL (10, 2) NOT NULL,
    discount FLOAT   
);
	
    