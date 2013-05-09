use DBmobile;

DROP TABLE Users;
CREATE TABLE Users(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	password VARCHAR(20),
	age int,	
	gender VARCHAR(20),
	postal_code VARCHAR(20),
	browser VARCHAR(100),
	source_ip VARCHAR(15),
 	created TIMESTAMP DEFAULT NOW()
); 

DROP TABLE Questionaire;
CREATE TABLE Questionaire(
	id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	userid int,
  step1 double,
  step2 double,
  step3 double,
  step4 double,
  step5 double,
  step6 double,
  step7 double,
	scale7shq double,
	diener double,
	love int,
	health int,
	job int,
	browser VARCHAR(100),
	source_ip VARCHAR(15),
 	created TIMESTAMP DEFAULT NOW()
);

DROP TABLE Reminder;
CREATE TABLE Reminder(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	userid int,
	grade int,
	browser VARCHAR(100),
	source_ip VARCHAR(15),
 	created TIMESTAMP DEFAULT NOW()
);
