-- Create a stored procedure `ComputeAverageScoreForUser` that computes
-- and store the average score for a student.
-- procedure `ComputeAverageScoreForUser`:
-- user_id: users.id value

delimiter //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE average FLOAT;

    SET average = (SELECT AVG(score) FROM corrections 
        WHERE user_id = user_id);
    UPDATE users
        SET average_score = average
        WHERE id = user_id;
END //
delimiter ;


