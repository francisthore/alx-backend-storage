-- Creates a stored procedure that add
-- a new correction for a student
DELIMITER //
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
  DECLARE project_exists INT;
  DECLARE p_id INT;
  SELECT EXISTS (
    SELECT 1
    FROM projects
    WHERE projects.name = project_name
  ) INTO project_exists;
  IF project_exists = 0 THEN
    INSERT INTO projects (name) VALUES (project_name);
  END IF;
  SELECT id from projects where projects.name = project_name INTO p_id;

  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, p_id, score);

END //

DELIMITER ;
