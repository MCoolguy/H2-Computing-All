SELECT competitor.name, scores.score
FROM competitor, scores
WHERE competitor.id = scores.id AND round = 1
ORDER BY scores.score DESC;

SELECT competitor.name, scores.score
FROM competitor, scores
WHERE competitor.id = scores.id AND round = 2
ORDER BY scores.score DESC;

SELECT competitor.name, scores.score
FROM competitor, scores
WHERE competitor.id = scores.id AND round = 3
ORDER BY scores.score DESC;