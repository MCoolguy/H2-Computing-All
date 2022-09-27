CREATE TABLE school( SchoolCode INTEGER PRIMARY KEY, Name STRING , Address STRING)
;
CREATE TABLE staff( SchoolCode INTEGER, Name STRING, Department STRING, Contact STRING, FOREIGN KEY(SchoolCode) REFERENCES school(SchoolCode))