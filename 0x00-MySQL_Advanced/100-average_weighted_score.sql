-- Create a stored procedure `ComputeAverageWeightedScoreForUser`
-- that computes and store the average weighted score for a student
-- parameter:
-- user_id: users.id
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE score FLOAT;
    DECLARE weight INT;
    DECLARE done BOOL DEFAULT FALSE;

    DECLARE cur CURSOR FOR 
        SELECT corrections.score, projects.weight 
        FROM corrections
        INNER JOIN projects ON projects.id = corrections.project_id
        WHERE corrections.user_id = user_id;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO score, weight;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET total_score = total_score + (score * weight);
        SET total_weight = total_weight + weight;
    END LOOP;

    CLOSE cur;

    IF total_weight > 0 THEN
        UPDATE users
            SET average_score = total_score / total_weight
            WHERE id = user_id;
    END IF;
END //
DELIMITER ;