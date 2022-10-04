SELECT competitor.name, SUM(scores.score)/COUNT(scores.score)
FROM competitor, scores
WHERE competitor.id = scores.id
GROUP BY name
ORDER BY name ASC