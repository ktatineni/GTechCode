USE word_association;

ALTER TABLE wordassociation_ac
ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST;

SELECT * FROM wordassociation_ac
WHERE source = "AC";

SELECT * FROM wordassociation_ac
WHERE source = "BC";

SELECT * FROM wordassociation_ac
WHERE source = "CC";

SELECT * FROM wordassociation_ac
WHERE author >= 0 AND author <= 20;

SELECT * FROM wordassociation_ac
WHERE word1 = "pie" OR word2 = "pie";

SELECT MIN(id) FROM wordassociation_ac
WHERE source = "CC";

-- Find how many rows have an author of 12
SELECT COUNT(author)  FROM wordassociation_ac
WHERE author = 12;

