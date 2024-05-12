-- Create a stored procedure `ComputeAverageWeightedScoreForUsers`
-- that computes and store the average weighted score for all students

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE done BOOL DEFAULT FALSE;

    DECLARE cur CURSOR FOR 
        SELECT id from users;
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SELECT 
            SUM(corrections.score * projects.weight), SUM(projects.weight)
        INTO
            total_score, total_weight
        FROM 
            corrections
        INNER JOIN 
            projects ON projects.id = corrections.project_id
        WHERE 
            corrections.user_id = user_id;

        
        IF total_weight IS NOT NULL THEN
            UPDATE users
                SET average_score = total_score / total_weight
                WHERE users.id = user_id;
        END IF;

    END LOOP;

    CLOSE cur;

END //
DELIMITER ;