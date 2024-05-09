-- Create a stored procedure AddBonus that adds a new correction for a student.
-- AddBonus is taking 3 inputs:
-- user_id: users.id
-- project_name: a new or already exists projects. if no `projects.name`
-- found in the table, create it.
-- score , the score value for the correction

delimiter //
CREATE PROCEDURE AddBonus(
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score FLOAT
)
BEGIN
    DECLARE project_id INT;

    SET project_id = (SELECT id FROM projects 
        WHERE projects.name = project_name);

    IF project_id IS NOT NULL THEN
        INSERT INTO corrections (user_id, project_id, score)
            VALUES (user_id, project_id, score);
        ELSE
            INSERT INTO projects (name) VALUES (project_name);
            SET project_id = (SELECT id FROM projects
                WHERE projects.name = project_name);
            INSERT INTO corrections (user_id, project_id, score)
                VALUES (user_id, project_id, score);
    END IF;
END //
delimiter ;
    

    


