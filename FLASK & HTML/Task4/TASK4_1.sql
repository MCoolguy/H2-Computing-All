DROP TABLE IF EXISTS "Location";
DROP TABLE IF EXISTS "Visitor";
PRAGMA foreign_keys = ON;

CREATE TABLE "Location"(
	"LocationID" TEXT,
	"Name" TEXT, 
	"Address" TEXT, 
	"URL" TEXT,
	PRIMARY KEY ("LocationID")
);
		
CREATE TABLE "Visitor"(
	"NRIC" TEXT,
	"LocationID" TEXT,
	"Name" TEXT,
	"Contact" TEXT,
	"Date" TEXT,
	"TimeIn" TEXT,
	"TimeOut" TEXT,
	PRIMARY KEY("NRIC","LocationID","Date","TimeIn")
	FOREIGN KEY("LocationID") REFERENCES "Location"("LocationID")
);