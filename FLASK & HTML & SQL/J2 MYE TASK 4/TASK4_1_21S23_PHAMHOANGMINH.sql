PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS "School";
DROP TABLE IF EXISTS "Subject";

CREATE TABLE "School" (
	"SchoolID"	INTEGER,
	"Name"	TEXT,
	"Zone"	TEXT,
	"Level"	TEXT,
	"YearsOfStudy" INT,
	PRIMARY KEY("SchoolID")
);

CREATE TABLE "Subject" (
	"SchoolID"	INTEGER,
	"SubjectName"	TEXT,
	PRIMARY KEY("SchoolID","SubjectName")
	FOREIGN KEY("SchoolID") REFERENCES "School"("SchoolID")
);