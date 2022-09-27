DROP TABLE IF EXISTS 'Arts';
DROP TABLE IF EXISTS 'Cultural';
DROP TABLE IF EXISTS 'Sports';
DROP TABLE IF EXISTS 'Registration';

CREATE TABLE 'Registration' (
	'StudentID'	TEXT NOT NULL,
	'Type'	TEXT NOT NULL,
	'Venue'	TEXT NOT NULL,
	'Session'	TEXT NOT NULL,
	PRIMARY KEY('StudentID')
);

CREATE TABLE 'Arts' (
	'ID'	TEXT NOT NULL,
	'Performance'	TEXT NOT NULL,
	PRIMARY KEY('ID'),
	FOREIGN KEY('ID') REFERENCES 'Registration'('StudentID')
);

CREATE TABLE 'Cultural' (
	'ID'	INTEGER NOT NULL,
	'Race'	TEXT NOT NULL,
	PRIMARY KEY('ID'),
	FOREIGN KEY('ID') REFERENCES 'Registration'('StudentID')
);
CREATE TABLE 'Sports' (
	'ID'	TEXT NOT NULL,	
	'Contact'	TEXT NOT NULL,
	'Cost'	INTEGER NOT NULL,
	PRIMARY KEY('ID'),
	FOREIGN KEY('ID') REFERENCES 'Registration'('StudentID')
);
