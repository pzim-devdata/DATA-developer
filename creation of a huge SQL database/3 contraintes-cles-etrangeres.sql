USE ZARA;

ALTER TABLE products2
ADD FOREIGN KEY fk_categories_products(category_id) REFERENCES categories2 (category_id) -- ON DELETE CASCADE ON UPDATE CASCADE
;
ALTER TABLE products2
ADD FOREIGN KEY fk_brands_products(brand_id) REFERENCES brands2 (brand_id) -- ON DELETE CASCADE ON UPDATE CASCADE
;
ALTER TABLE stocks2
ADD FOREIGN KEY fk_products_stocks (product_id) REFERENCES products2 (product_id) -- ON DELETE CASCADE ON UPDATE CASCADE
;
ALTER TABLE orders1
ADD FOREIGN KEY fk_customers_orders (customer_id) REFERENCES customers1 (customer_id) -- ON DELETE CASCADE ON UPDATE CASCADE
;
ALTER TABLE orders1
ADD FOREIGN KEY fk_staffs_orders (staff_id) REFERENCES staffs1 (staff_id) -- ON DELETE CASCADE ON UPDATE CASCADE
;
ALTER TABLE order_items1
ADD FOREIGN KEY fk_orders_order_items (order_id) REFERENCES orders1 (order_id) -- ON DELETE CASCADE ON UPDATE CASCADE
;
ALTER TABLE orders1
ADD FOREIGN KEY fk_stores_orders (store_id) REFERENCES stores1 (store_id) -- ON DELETE CASCADE ON UPDATE CASCADE
;
ALTER TABLE stocks2
ADD FOREIGN KEY fk_stores_stocks (store_id) REFERENCES stores1 (store_id) -- ON DELETE CASCADE ON UPDATE CASCADE
;
ALTER TABLE order_items1
ADD FOREIGN KEY fk_products_order_items (product_id) REFERENCES products2 (product_id)
;
ALTER TABLE staffs1
ADD FOREIGN KEY fk_stores_staffs (store_id) REFERENCES stores1 (store_id)
;
ALTER TABLE staffs1
ADD FOREIGN KEY fk__staffs (manager_id) REFERENCES staffs1 (staff_id);

