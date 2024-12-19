
CREATE_USER = """
    INSERT INTO users (username, password_hash, role) 
    VALUES (%s, %s, %s) RETURNING id;
"""

GET_USER_BY_USERNAME = """
    SELECT id, username, password_hash, role FROM users WHERE username = %s;
"""

GET_MENU = """
SELECT id, name, description, price, available,
       'https://via.placeholder.com/150' AS image_url
FROM product WHERE available = TRUE;
"""

CREATE_ORDER = """
    INSERT INTO orders (user_id, product_id, quantity, status) 
    VALUES (%s, %s, %s, 'pending') RETURNING id;
"""

GET_ORDERS = """
    SELECT o.id, o.status, m.name, m.price, o.quantity
    FROM orders o
    JOIN product m ON o.product_id = m.id
    WHERE o.user_id = %s;
"""
ADD_TO_CART = """
INSERT INTO cart (username, item_name, quantity) 
VALUES (%s, %s, %s)
"""

GET_CART_ITEMS = """
SELECT m.name AS item_name, c.quantity, m.price, c.created_at
FROM cart c
JOIN product m ON c.product_id = m.id
WHERE c.user_id = (SELECT id FROM users WHERE username = %s);
"""

ADD_TO_CART = """
INSERT INTO cart (user_id, product_id, quantity) 
VALUES (
    (SELECT id FROM users WHERE username = %s),
    (SELECT id FROM product WHERE name = %s),
    %s
);
"""
DELETE_FROM_CART = """
DELETE FROM cart 
WHERE user_id = (SELECT id FROM users WHERE username = %s) 
AND product_id = (SELECT id FROM product WHERE name = %s)
RETURNING *;
"""

GET_REVIEWS = """
SELECT user_id, product_id, rating, review, created_at FROM reviews
ORDER BY created_at DESC;
"""

GET_ORDERS = """
SELECT id, user_id, product_id, quantity, status, created_at FROM orders
ORDER BY created_at DESC;
"""

