SELECT competitor.name as Name, sum(scores.score) as Total, SUM(scores.score)>250 as Qualified
FROM competitor, scores
WHERE competitor.id = scores.id 
GROUP BY name 
ORDER BY Qualified DESC, Total DESC