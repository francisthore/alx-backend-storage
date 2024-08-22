-- Creates a trigger that resets the valid_email 
-- only after the email field has been changed
DELIMITER //
CREATE TRIGGER check_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF OLD.email <> NEW.email THEN
    SET NEW.valid_email = 0;
  END IF;
END //
DELIMITER ;
