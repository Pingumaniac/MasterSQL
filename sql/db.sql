CREATE TABLE IF NOT EXISTS Account (
  userName VARCHAR(256) NOT NULL,
  isAdmin BOOLEAN,
  PRIMARY KEY (userName)
); 

CREATE TABLE IF NOT EXISTS UserAccount (
  fullName VARCHAR(1000) NOT NULL,
  userName VARCHAR(256) NOT NULL,
  password VARCHAR(256) NOT NULL,
  email VARCHAR(256) NOT NULL,
  phoneNumber VARCHAR(11) NOT NULL,
  profilePictureURL MEDIUMTEXT,
  PRIMARY KEY (userName),
  FOREIGN KEY (userName) REFERENCES Account(userName) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS AdminAccount (
  fullName VARCHAR(1000) NOT NULL,
  userName VARCHAR(256) NOT NULL,
  password VARCHAR(256) NOT NULL,
  email VARCHAR(256) NOT NULL,
  phoneNumber VARCHAR(11) NOT NULL,
  profilePictureURL MEDIUMTEXT,
  jobTitle VARCHAR(256) NOT NULL,
  PRIMARY KEY (userName),
  FOREIGN KEY (userName) REFERENCES Account(userName) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Test1Scores (
  userName VARCHAR(256) NOT NULL, 
  q1Status TINYINT,
  q2Status TINYINT,
  q3Status TINYINT,
  q4Status TINYINT,
  q5Status TINYINT,
  q6Status TINYINT,
  q7Status TINYINT,
  q8Status TINYINT,
  q9Status TINYINT,
  q10Status TINYINT,
  dateAndTime TIMESTAMP NOT NULL,
  PRIMARY KEY (userName, dateAndTime),
  FOREIGN KEY (userName) REFERENCES Account(userName) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS Test2Scores (
  userName VARCHAR(256) NOT NULL, 
  q1Status TINYINT,
  q2Status TINYINT,
  q3Status TINYINT,
  q4Status TINYINT,
  q5Status TINYINT,
  q6Status TINYINT,
  q7Status TINYINT,
  q8Status TINYINT,
  q9Status TINYINT,
  q10Status TINYINT,
  dateAndTime TIMESTAMP NOT NULL,
  PRIMARY KEY (userName, dateAndTime),
  FOREIGN KEY (userName) REFERENCES Account(userName) ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS Test3Scores (
  userName VARCHAR(256) NOT NULL, 
  q1Status TINYINT,
  q2Status TINYINT,
  q3Status TINYINT,
  q4Status TINYINT,
  q5Status TINYINT,
  dateAndTime TIMESTAMP NOT NULL,
  PRIMARY KEY (userName, dateAndTime),
  FOREIGN KEY (userName) REFERENCES Account(userName) ON DELETE NO ACTION
);

/* Example Table and Queries for Learn SQL Contents */
CREATE TABLE IF NOT EXISTS SmartPhones (
  Model_name VARCHAR(256) NOT NULL,
  Manufacturer VARCHAR(256) NOT NULL,
  Display_size DOUBLE NOT NULL,
  PRIMARY KEY (Model_name)
);

INSERT INTO SmartPhones (Model_name, Manufacturer, Display_size) VALUES ('iPhone 13 Pro Max', 'Apple', 6.7);
INSERT INTO SmartPhones (Model_name, Manufacturer, Display_size) VALUES ('iPhone 13 Pro', 'Apple', 6.1);
INSERT INTO SmartPhones (Model_name, Manufacturer, Display_size) VALUES ('iPhone 13', 'Apple', 6.1);
INSERT INTO SmartPhones (Model_name, Manufacturer, Display_size) VALUES ('iPhone 13 Mini', 'Apple', 5.4);
INSERT INTO SmartPhones (Model_name, Manufacturer, Display_size) VALUES ('iPhone 12 Mini', 'Apple', 5.4);
INSERT INTO SmartPhones (Model_name, Manufacturer, Display_size) VALUES ('iPhone 11 Mini', 'Apple', 5.4);
INSERT INTO SmartPhones (Model_name, Manufacturer, Display_size) VALUES ('iPhone SE2', 'Apple', 4.7);

SELECT * FROM SmartPhones ORDER BY Display_size DESC;
SELECT * FROM SmartPhones;
SELECT EXISTS(SELECT Model_name FROM SmartPhones WHERE Model_name='iPhone 13') AS Existence_of_iPhone_13;
SELECT EXISTS(SELECT Model_name FROM SmartPhones WHERE Model_name='iPhone 14') AS Existence_of_iPhone_14;
SELECT DISTINCT Display_size FROM SmartPhones;
SELECT DISTINCT Display_size FROM SmartPhones ORDER BY Display_size ASC;
SELECT COUNT(DISTINCT Display_size) AS No_Of_SmartPhones_With_Distinct_Display_Size FROM SmartPhones;

CREATE TABLE IF NOT EXISTS iPads (
  Model_name VARCHAR(256) NOT NULL,
  Manufacturer VARCHAR(256) NOT NULL,
  Display_size DOUBLE NOT NULL,
  PRIMARY KEY (Model_name)
);

INSERT INTO iPads (Model_name, Manufacturer, Display_size) VALUES ('iPad Pro 12.9', 'Apple', 12.9);
INSERT INTO iPads (Model_name, Manufacturer, Display_size) VALUES ('iPad Pro 11', 'Apple', 11);
INSERT INTO iPads (Model_name, Manufacturer, Display_size) VALUES ('iPad Air', 'Apple', 10.9);
INSERT INTO iPads (Model_name, Manufacturer, Display_size) VALUES ('iPad', 'Apple', 10.2);
INSERT INTO iPads (Model_name, Manufacturer, Display_size) VALUES ('iPad mini', 'Apple', 7.9);

SELECT * FROM iPads ORDER BY Display_size DESC;

UPDATE iPads SET Display_size = 8.3 WHERE Model_name = 'iPad mini';

CREATE TABLE IF NOT EXISTS Current_iPads (
  Model_name VARCHAR(256) NOT NULL,
  Manufacturer VARCHAR(256) NOT NULL,
  Display_size DOUBLE NOT NULL,
  PRIMARY KEY (Model_name)
);

INSERT INTO Current_iPads (Model_name, Manufacturer, Display_size) VALUES ('iPad Pro 12.9 (5th generation)', 'Apple', 12.9);
INSERT INTO Current_iPads (Model_name, Manufacturer, Display_size) VALUES ('iPad Pro 11 (3th generation)', 'Apple', 11);
INSERT INTO Current_iPads (Model_name, Manufacturer, Display_size) VALUES ('iPad Air (4th generation)', 'Apple', 10.9);
INSERT INTO Current_iPads (Model_name, Manufacturer, Display_size) VALUES ('iPad (9th generation)', 'Apple', 10.2);
INSERT INTO Current_iPads (Model_name, Manufacturer, Display_size) VALUES ('iPad mini (6th generation)', 'Apple', 8.3);
INSERT INTO Current_iPads (Model_name, Manufacturer, Display_size) VALUES ('iPad mini (5th generation)', 'Apple', 7.9);

SELECT * FROM Current_iPads ORDER BY Display_size DESC;

DELETE FROM Current_iPads WHERE Model_name = 'iPad mini (5th generation)';

CREATE TABLE IF NOT EXISTS Consumer (
  consumerID VARCHAR(256) NOT NULL,
  consumerFullName VARCHAR(256) NOT NULL,
  PRIMARY KEY (consumerID)
);

CREATE TABLE IF NOT EXISTS Product (
  productID VARCHAR(256) NOT NULL,
  productName VARCHAR(256) NOT NULL,
  PRIMARY KEY (productID)
);

CREATE TABLE IF NOT EXISTS Purchased (
  consumerID VARCHAR(256) NOT NULL,
  productID VARCHAR(256) NOT NULL,
  PRIMARY KEY (consumerID, productID),
  FOREIGN KEY (consumerID) REFERENCES Consumer(consumerID),
  FOREIGN KEY (productID) REFERENCES Product(productID)
 );

CREATE TABLE IF NOT EXISTS DBMS (
  StudentID SMALLINT NOT NULL,
  StudentName VARCHAR(256) NOT NULL,
  Grade VARCHAR(5) NOT NULL,
  PRIMARY KEY (StudentID)
);

INSERT INTO DBMS VALUES (1001, 'Aaron', 'A+');
INSERT INTO DBMS VALUES (1002, 'Bash', 'A');
INSERT INTO DBMS VALUES (1003, 'Claire', 'A-');
INSERT INTO DBMS VALUES (1004, 'Darwin', 'B+');
INSERT INTO DBMS VALUES (1005, 'Euler', 'B');

CREATE TABLE IF NOT EXISTS HCI (
  StudentID SMALLINT NOT NULL,
  StudentName VARCHAR(256) NOT NULL,
  Grade VARCHAR(5) NOT NULL,
  PRIMARY KEY (StudentID)
);

INSERT INTO HCI VALUES (1001, 'Aaron', 'A');
INSERT INTO HCI VALUES (1002, 'Bash', 'A-');
INSERT INTO HCI VALUES (1003, 'Claire', 'A+');
INSERT INTO HCI VALUES (1006, 'Fortran', 'C+');
INSERT INTO HCI VALUES (1007, 'Haskell', 'F');

SELECT DBMS.StudentID AS StudentID, DBMS.StudentName AS StudentName, DBMS.Grade, HCI.Grade FROM DBMS INNER JOIN HCI ON DBMS.StudentID = HCI.StudentID;
SELECT DBMS.StudentID AS StudentID, DBMS.StudentName AS StudentName, DBMS.Grade, HCI.Grade FROM DBMS LEFT JOIN HCI ON DBMS.StudentID = HCI.StudentID;
SELECT HCI.StudentID AS StudentID, HCI.StudentName AS StudentName, DBMS.Grade AS DBMS_Grade, HCI.Grade AS HCI_Grade FROM DBMS RIGHT JOIN HCI ON DBMS.StudentID = HCI.StudentID;
(SELECT DBMS.StudentID AS StudentID, DBMS.StudentName AS StudentName, DBMS.Grade, HCI.Grade FROM DBMS LEFT JOIN HCI ON DBMS.StudentID = HCI.StudentID)
UNION
(SELECT HCI.StudentID AS StudentID, HCI.StudentName AS StudentName, DBMS.Grade AS DBMS_Grade, HCI.Grade AS HCI_Grade FROM DBMS RIGHT JOIN HCI ON DBMS.StudentID = HCI.StudentID);

SELECT * FROM DBMS WHERE StudentID IN (SELECT StudentID FROM HCI);
SELECT * FROM DBMS WHERE StudentID NOT IN (SELECT StudentID FROM HCI);

CREATE TABLE IF NOT EXISTS ElectricCars (
  carName VARCHAR(100) NOT NULL,
  manufacturer VARCHAR(100) NOT NULL,
  PRIMARY KEY (carName)
);

INSERT INTO ElectricCars VALUES ('EQA', 'Mercedes-Benz');
INSERT INTO ElectricCars VALUES ('EQB', 'Mercedes-Benz');
INSERT INTO ElectricCars VALUES ('EQC', 'Mercedes-Benz');
INSERT INTO ElectricCars VALUES ('EQE', 'Mercedes-Benz');
INSERT INTO ElectricCars VALUES ('EQS', 'Mercedes-Benz');
INSERT INTO ElectricCars VALUES ('iX', 'BMW');
INSERT INTO ElectricCars VALUES ('iX3', 'BMW');
INSERT INTO ElectricCars VALUES ('e-tron', 'Audi');
INSERT INTO ElectricCars VALUES ('e-tron GT', 'Audi');
INSERT INTO ElectricCars VALUES ('Q4 e-tron', 'Audi');
INSERT INTO ElectricCars VALUES ('Q4 Sportback e-tron', 'Audi');
INSERT INTO ElectricCars VALUES ('Model S', 'Tesla');
INSERT INTO ElectricCars VALUES ('Model 3', 'Tesla');
INSERT INTO ElectricCars VALUES ('Model X', 'Tesla');
INSERT INTO ElectricCars VALUES ('Model Y', 'Tesla');
INSERT INTO ElectricCars VALUES ('Cybertruck', 'Tesla');
INSERT INTO ElectricCars VALUES ('Roadster', 'Tesla');
INSERT INTO ElectricCars VALUES ('Mustang Mach-E', 'Ford');

SELECT manufacturer, COUNT(carName) AS no_of_electic_cars_on_sale FROM ElectricCars GROUP BY manufacturer;
SELECT manufacturer FROM ElectricCars GROUP BY manufacturer HAVING COUNT(carName) >= 3;
SELECT manufacturer FROM ElectricCars WHERE manufacturer <> 'TESLA' GROUP BY manufacturer HAVING COUNT(carName) >= 3;
SELECT manufacturer FROM ElectricCars GROUP BY manufacturer HAVING COUNT(carName) >= 3 AND manufacturer <> 'TESLA' ;

/* SQL queries for creating tables and inserting data for the testing part */

CREATE TABLE IF NOT EXISTS Apple_M_Series (
  chipName VARCHAR(10) NOT NULL,
  PRIMARY KEY (chipName)
);

INSERT INTO Apple_M_Series VALUES ('M1');
INSERT INTO Apple_M_Series VALUES ('M1 Pro');
INSERT INTO Apple_M_Series VALUES ('M1 Max');

CREATE TABLE IF NOT EXISTS MacBookPro (
  modelName VARCHAR(100) NOT NULL,
  chipName VARCHAR(10) NOT NULL,
  SSD INTEGER NOT NULL,
  price INTEGER,
  hasNotch BOOLEAN,
  PRIMARY KEY (modelName, chipName, SSD),
  FOREIGN KEY (chipName) REFERENCES Apple_M_Series(chipName)
);

INSERT INTO MacBookPro VALUES ('MacBook Pro 13', 'M1', '256', 1299, 0);
INSERT INTO MacBookPro VALUES ('MacBook Pro 13', 'M1', '512', 1499, 0);
INSERT INTO MacBookPro VALUES ('MacBook Pro 14', 'M1 Pro', '512', 1999, 1);
INSERT INTO MacBookPro VALUES ('MacBook Pro 14', 'M1 Pro', '1024', 2499, 1);
INSERT INTO MacBookPro VALUES ('MacBook Pro 16', 'M1 Pro', '512', 2499, 1);
INSERT INTO MacBookPro VALUES ('MacBook Pro 16', 'M1 Pro', '1024', 2699, 1);
INSERT INTO MacBookPro VALUES ('MacBook Pro 16', 'M1 Max', '1024', 3499, 1);

CREATE TABLE IF NOT EXISTS Mathematics (
  StudentID SMALLINT NOT NULL,
  StudentName VARCHAR(256) NOT NULL,
  GPA FLOAT,
  PRIMARY KEY (StudentID)
);

INSERT INTO Mathematics VALUES (101, 'Socrates', 2.33);
INSERT INTO Mathematics VALUES (102, 'Plato', 4.33);
INSERT INTO Mathematics VALUES (103, 'Aristotle', 4.33);
INSERT INTO Mathematics VALUES (104, 'Cicero', 3.33);
INSERT INTO Mathematics VALUES (105, 'Descartes', 4.33);

CREATE TABLE IF NOT EXISTS English (
  StudentID SMALLINT NOT NULL,
  StudentName VARCHAR(256) NOT NULL,
  GPA FLOAT,
  PRIMARY KEY (StudentID)
);

INSERT INTO English VALUES (101, 'Socrates', 1.67);
INSERT INTO English VALUES (102, 'Plato', 1.67);
INSERT INTO English VALUES (103, 'Aristotle', 2.0);
INSERT INTO English VALUES (106, 'Spinoza', 4.33);
INSERT INTO English VALUES (107, 'Kant', 4);

CREATE TABLE IF NOT EXISTS iPhone13ProMaxCase (
  caseName VARCHAR(100) NOT NULL,
  manufacturer VARCHAR(100) NOT NULL,
  price FLOAT,
  PRIMARY KEY (caseName)
);

INSERT INTO iPhone13ProMaxCase VALUES ('iPhone 13 Pro Max Silicone Case with MagSafe', 'Apple', 49);
INSERT INTO iPhone13ProMaxCase VALUES ('iPhone 13 Pro Max Leather Case with MagSafe', 'Apple', 59);
INSERT INTO iPhone13ProMaxCase VALUES ('iPhone 13 Pro Max Clear Case with MagSafe', 'Apple', 49);
INSERT INTO iPhone13ProMaxCase VALUES ('Otterbox Aneu Series Case with MagSafe for iPhone 13 Pro Max', 'Otterbox', 49.95);
INSERT INTO iPhone13ProMaxCase VALUES ('Otterbox Figura Series Case with MagSafe for iPhone 13 Pro Max', 'Otterbox', 49.95);
INSERT INTO iPhone13ProMaxCase VALUES ('Tech21 Evo Art Floral Bouquet Case for iPhone 13 Pro Max', 'Tech 21', 49.95);
INSERT INTO iPhone13ProMaxCase VALUES ('Otterbox iPhone 13 Pro Max Lumen Series with MagSafe', 'Otterbox', 49.95);

CREATE TABLE IF NOT EXISTS AirTagCase (
  caseName VARCHAR(100) NOT NULL,
  pack TINYINT NOT NULL,
  manufacturer VARCHAR(100) NOT NULL,
  price FLOAT,
  PRIMARY KEY (caseName, pack)
);

INSERT INTO AirTagCase VALUES ('AirTag Leather Key Ring', 1, 'Apple', 35);
INSERT INTO AirTagCase VALUES ('AirTag Loop', 1, 'Apple', 29);
INSERT INTO AirTagCase VALUES ('AirTag Leather Loop', 1, 'Apple', 39);
INSERT INTO AirTagCase VALUES ('Belkin Secure Holder with Strap for AirTag', 1, 'Belkin', 12.95);
INSERT INTO AirTagCase VALUES ('Belkin Secure Holder with Key Ring for AirTag', 1, 'Belkin', 12.95);
INSERT INTO AirTagCase VALUES ('Belkin Secure Holder with Key Ring for AirTag', 4, 'Belkin', 39.95);
INSERT INTO AirTagCase VALUES ('OtterBox Rugged Case for AirTag', 1, 'OtterBox', 19.95);
INSERT INTO AirTagCase VALUES ('Incase Woolenex Key Clip for AirTag', 1, 'Incase', 19.95);
INSERT INTO AirTagCase VALUES ('Belkin Secure Holder with Wire Cable for AirTag', 1, 'Belkin', 19.95);
INSERT INTO AirTagCase VALUES ('Tech21 Evo Clear case for AirTag', 2, 'Tech 21', 29.95);

/* Sample Answer Queries for Test 1 */
SELECT * FROM Apple_M_Series;
SELECT COUNT(*) AS No_of_Apple_M_Series FROM Apple_M_Series;
SELECT modelName, chipName, SSD, price FROM MacBookPro WHERE hasNotch = 1;
SELECT modelName, chipName, SSD, price FROM MacBookPro WHERE NOT hasNotch = 1;
SELECT * FROM MacBookPro ORDER BY price DESC;
SELECT * FROM MacBookPro ORDER BY price ASC;
SELECT COUNT(*) AS "No_of_MacBook_Pro" FROM MacBookPro;
SELECT MAX(price) AS "maximum_price" FROM MacBookPro;
SELECT MIN(price) AS "minimum_price" FROM MacBookPro;
SELECT MIN(price) AS "minimum_price" FROM MacBookPro WHERE modelName = 'MacBook Pro 16';

/* Sample Answer Queries for Test 2 */
SELECT Mathematics.StudentID, Mathematics.StudentName, Mathematics.GPA AS Math_GPA, English.GPA AS English_GPA 
FROM Mathematics INNER JOIN English ON Mathematics.StudentID = English.StudentID;

SELECT Mathematics.StudentID, Mathematics.StudentName, Mathematics.GPA AS Math_GPA, English.GPA AS English_GPA 
FROM Mathematics LEFT JOIN English ON Mathematics.StudentID = English.StudentID;

SELECT English.StudentID, English.StudentName, Mathematics.GPA AS Math_GPA, English.GPA AS English_GPA 
FROM Mathematics RIGHT JOIN English ON Mathematics.StudentID = English.StudentID;

(SELECT Mathematics.StudentID, Mathematics.StudentName, Mathematics.GPA AS Math_GPA, English.GPA AS English_GPA 
FROM Mathematics LEFT JOIN English ON Mathematics.StudentID = English.StudentID) UNION
(SELECT English.StudentID, English.StudentName, Mathematics.GPA AS Math_GPA, English.GPA AS English_GPA 
FROM Mathematics RIGHT JOIN English ON Mathematics.StudentID = English.StudentID);

SELECT AVG(GPA) AS "average_gpa" FROM Mathematics WHERE StudentID IN (SELECT StudentID FROM English);
SELECT AVG(GPA) AS "average_gpa" FROM Mathematics WHERE StudentID NOT IN (SELECT StudentID FROM English);
SELECT MAX(GPA) AS "highest_gpa" FROM Mathematics WHERE StudentID IN (SELECT StudentID FROM English);
SELECT MIN(GPA) AS "lowest_gpa" FROM Mathematics WHERE StudentID IN (SELECT StudentID FROM English);
SELECT MAX(GPA) AS "highest_gpa" FROM Mathematics WHERE StudentID NOT IN (SELECT StudentID FROM English);
SELECT MIN(GPA) AS "lowest_gpa" FROM Mathematics WHERE StudentID NOT IN (SELECT StudentID FROM English);

/* Sample Answer Queries for Test 3 */
SELECT manufacturer, COUNT(caseName) AS  Number_of_iPhone_13_Pro_Max_Cases FROM iPhone13ProMaxCase GROUP BY manufacturer;
SELECT manufacturer FROM iPhone13ProMaxCase GROUP BY manufacturer HAVING COUNT(caseName) >= 2;
SELECT manufacturer FROM iPhone13ProMaxCase WHERE manufacturer <> 'Apple' GROUP BY manufacturer HAVING COUNT(caseName) >= 2;

SELECT manufacturer, COUNT(caseName) AS  Number_of_AirTag_Cases FROM AirTagCase WHERE AirTagCase.manufacturer IN 
(SELECT manufacturer FROM iPhone13ProMaxCase) GROUP BY manufacturer;

SELECT manufacturer, COUNT(caseName) AS  Number_of_AirTag_Cases FROM AirTagCase WHERE AirTagCase.manufacturer NOT IN 
(SELECT manufacturer FROM iPhone13ProMaxCase) GROUP BY manufacturer;