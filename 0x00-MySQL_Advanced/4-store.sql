-- Create a trigger that decrease the quantity of an item after
-- adding a new order

delimiter //
CREATE TRIGGER decrease_quantity 
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
        SET quantity = quantity - NEW.number
        WHERE items.name = NEW.item_name;
END //
delimiter ;

