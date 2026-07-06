CREATE TABLE Teams(team_id INT, team_name VARCHAR(50));
INSERT INTO Teams VALUES(1,'RCB'),(2,'MI'),(3,'CSK');
-- table2:scores
CREATE TABLE Scores(team_id INT, matches INT, runs INT);
INSERT INTO Scores VALUES(1,5,100), (2,5,135), (3,5,60);

-- JOIN:dono table ko jodo
SELECT Teams.team_name, Scores.matches, Scores.runs
FROM Teams
JOIN Scores ON Teams.team_id=Scores.team_id;
