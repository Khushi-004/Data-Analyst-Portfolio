CREATE TABLE ipl_runs (PlayerId INT, Name VARCHAR(50), Team VARCHAR(50), Runs INT);
INSERT INTO ipl_runs VALUES (1, 'Virat', 'RCB', 80), (2, 'Rohit', 'Mi', 45),  (3, 'Dhoni', 'CSK', 60),  (4, 'Rahul', 'RCB', 100),  (5, 'Pant', 'MI', 90);
SELECT Team, SUM(Runs) as Total_Runs 
FROM ipl_runs 
GROUP BY Team 
ORDER BY Total_Runs DESC;
