SELECT * FROM orders;

INSERT INTO orders(order_id, customer_id, order_date, status)
VALUES(1, 1, "2026-01-01", "delivered");

INSERT INTO order_items(order_id, product_id, quantity, unit_price)
VALUES(1, 1, 1, 599),
		(1, 3, 2, 199);
		
SELECT * FROM order_items;

SELECT COUNT (*) FROM orders;

SELECT COUNT (*) FROM order_items;