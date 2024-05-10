-- Create a stored procedure `ComputeAverageScoreForUser` that computes
-- and store the average score for a student.
-- procedure `ComputeAverageScoreForUser`:
-- user_id: users.id value

delimiter //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    UPDATE users
        SET average_score = (SELECT AVG(score) FROM corrections 
            WHERE corrections.user_id = user_id)
        WHERE id = user_id;
END //
delimiter ;


