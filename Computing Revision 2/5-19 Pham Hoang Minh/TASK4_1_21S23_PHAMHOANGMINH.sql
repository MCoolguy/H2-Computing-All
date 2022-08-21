CREATE TABLE `School` (
	`SchoolD`	INTEGER,
	`Name`	TEXT,
	`Zone`	TEXT,
	`Level`	TEXT,
	`YearsOfStudy`	INTEGER,
	PRIMARY KEY(`SchoolD`)
);

CREATE TABLE `Subject` (
	`SchoolID`	INTEGER,
	`SubjectName`	TEXT,
	FOREIGN KEY(`SchoolID`) REFERENCES `School`(`SchoolD`)
);