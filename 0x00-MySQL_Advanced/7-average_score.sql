-- Creates a procedure that computes and store the average
-- score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  DECLARE avg_score DECIMAL (5,2);
  SELECT AVG(score)
  INTO avg_score
  FROM corrections
  WHERE corrections.user_id = user_id;

  SELECT avg_score as average_score
END //
DELIMITER ;
