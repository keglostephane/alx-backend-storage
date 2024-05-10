-- Create a function `SafeDiv` that divides and returns the first
-- by the second number or returns 0 is the second number is 
-- equal to 0.

delimiter //
CREATE FUNCTION SafeDiv(
    a INT,
    b INT
) RETURNS FLOAT DETERMINISTIC
BEGIN
    RETURN IF(b, a/b, 0);
END //
delimiter ;