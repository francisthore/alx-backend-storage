-- Creates a trigger that decreases the
-- quantity of an item after an order has been added
DELIMITER //
CREATE TRIGGER update_qty
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name;
END //
DELIMITER ;
