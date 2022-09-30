CREATE TABLE `Customer` (
	`Email`	TEXT,
	`FirstName`	TEXT,
	`LastName`	TEXT,
	`ContactNumber`	TEXT,
	`DOB`	TEXT,
	`Address`	TEXT,
	PRIMARY KEY(`Email`)
);
CREATE TABLE `CustomerRental` (
	`ID`	INTEGER,
	`Email`	TEXT,
	`StartDate`	TEXT,
	`EndDate`	TEXT,
	PRIMARY KEY(`ID`),
	FOREIGN KEY(`Email`) REFERENCES `Customer`(`Email`)
);
CREATE TABLE `Product` (
	`CatalogueNumber`	INTEGER,
	`Category`	TEXT,
	`Brand`	TEXT,
	`Size`	INTEGER,
	`Fee`	INTEGER,
	PRIMARY KEY(`CatalogueNumber`)
);
CREATE TABLE `ProductRental` (
	`ID`	INTEGER,
	`CatalogueNumber`	INTEGER,
	`Returned`	TEXT,
	PRIMARY KEY(`CatalogueNumber`,`ID`),
	FOREIGN KEY(`ID`) REFERENCES `CustomerRental`(`ID`),
	FOREIGN KEY(`CatalogueNumber`) REFERENCES `Product`(`CatalogueNumber`)
);