DROP TABLE IF EXISTS "schools";
DROP TABLE IF EXISTS "staff";
PRAGMA foreign_keys = ON;

CREATE TABLE "schools" (
	"SchoolCode"	INTEGER,
	"Name"	TEXT,
	"Address"	TEXT,
	PRIMARY KEY("SchoolCode")
);


CREATE TABLE "staff" (
	"SchoolCode"	INTEGER,
	"Name" TEXT,
	"Department" TEXT,
	"Contact" TEXT,
	PRIMARY KEY("SchoolCode", "Name")
	FOREIGN KEY("SchoolCode") REFERENCES "schools"("SchoolCode")
);