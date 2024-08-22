-- Divides 2 numbers
-- Safely and returns 0 if the quotient is 0
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS INT
BEGIN
  IF b = 0 THEN
    RETURN 0;
  END IF;
  RETURN a / b;
END //
DELIMITER ;
