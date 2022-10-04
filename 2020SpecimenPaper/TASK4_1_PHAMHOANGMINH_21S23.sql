
CREATE TABLE `Device` (
	`SerialNumber`	TEXT,
	`Type`	TEXT,
	`Model`	TEXT,
	`Location`	TEXT,
	`DateOfPurchase`	TEXT,
	`WrittenOff`	TEXT,
	PRIMARY KEY(`SerialNumber`)
);
CREATE TABLE `Laptop` (
	`Model`	TEXT,
	`Location`	TEXT,
	`DateOfPurchase`	TEXT,
	`WrittenOff`	TEXT,
	`WeightKg`	REAL,
	`SerialNumber`	TEXT,
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`)
);
CREATE TABLE `Monitor` (
	`Model`	TEXT,
	`Location`	TEXT,
	`DateOfPurchase`	TEXT,
	`WrittenOff`	TEXT,
	`DateCleaned`	TEXT,
	`SerialNumber`	TEXT,
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`)
);
CREATE TABLE `Printer` (
	`Model`	TEXT,
	`Location`	TEXT,
	`DateOfPurchase`	TEXT,
	`WrittenOff`	TEXT,
	`Toner`	TEXT,
	`DateChanged`	TEXT,
	`SerialNumber`	TEXT,
	FOREIGN KEY(`SerialNumber`) REFERENCES `Device`(`SerialNumber`)
);