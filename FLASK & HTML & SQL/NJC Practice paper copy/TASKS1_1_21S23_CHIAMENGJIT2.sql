BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "schools" (
	"SchoolCode"	INTEGER,
	"Name"	TEXT,
	"Address"	TEXT,
	PRIMARY KEY("SchoolCode")
);
CREATE TABLE IF NOT EXISTS "staff" (
	"SchoolCode"	INTEGER,
	"Name"	TEXT,
	"Department"	TEXT,
	"Contact"	TEXT,
	PRIMARY KEY("SchoolCode","Name"),
	FOREIGN KEY("SchoolCode") REFERENCES "schools"("SchoolCode")
);
COMMIT;
