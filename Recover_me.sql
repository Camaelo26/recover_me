-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: recover_me
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `AppointmentID` int NOT NULL AUTO_INCREMENT,
  `PatientID` int NOT NULL,
  `DoctorID` int NOT NULL,
  `AppointmentDate` datetime NOT NULL,
  `Status` enum('Scheduled','Completed','Cancelled','Pending') NOT NULL,
  PRIMARY KEY (`AppointmentID`),
  KEY `PatientID` (`PatientID`),
  KEY `DoctorID` (`DoctorID`),
  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`PatientID`) REFERENCES `patients` (`PatientID`),
  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`DoctorID`) REFERENCES `doctors` (`DoctorID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES (1,2,7,'2024-05-08 16:00:00','Scheduled'),(2,2,6,'2024-04-08 18:00:00','Pending'),(5,2,6,'2024-05-05 16:30:00','Pending'),(6,1,3,'2024-06-07 15:00:00','Scheduled'),(7,3,7,'2024-06-06 14:00:00','Cancelled'),(8,1,2,'2024-04-10 14:00:00','Scheduled');
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `DepartmentID` int NOT NULL AUTO_INCREMENT,
  `DepartmentName` varchar(100) NOT NULL,
  PRIMARY KEY (`DepartmentID`),
  UNIQUE KEY `DepartmentName` (`DepartmentName`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,'Cardiology'),(2,'Dermatology'),(4,'Neurology'),(5,'Pediathry'),(3,'Surgery');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `DoctorID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `DepartmentID` int NOT NULL,
  `ContactNumber` varchar(15) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`DoctorID`),
  UNIQUE KEY `UserID` (`UserID`),
  UNIQUE KEY `Email` (`Email`),
  KEY `DepartmentID` (`DepartmentID`),
  CONSTRAINT `doctors_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`),
  CONSTRAINT `doctors_ibfk_2` FOREIGN KEY (`DepartmentID`) REFERENCES `departments` (`DepartmentID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES (2,4,'Godfrey','osa',1,'987654321','osa@'),(3,5,'abena','Poku',3,'9725613215','Abe@'),(4,6,'Lincoln','william',5,'789456123','william@'),(5,7,'Liam','Noah',3,'654987321','Liam@'),(6,8,'Benjamin','Theodore',1,'321456987','Benj@'),(7,10,'Paul','jamaal',4,'7896541230','Jamaal@');
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `PatientID` int NOT NULL AUTO_INCREMENT,
  `UserID` int NOT NULL,
  `FirstName` varchar(50) NOT NULL,
  `LastName` varchar(50) NOT NULL,
  `DateOfBirth` date NOT NULL,
  `Gender` enum('Male','Female','Other') NOT NULL,
  `ContactNumber` varchar(15) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`PatientID`),
  UNIQUE KEY `UserID` (`UserID`),
  UNIQUE KEY `Email` (`Email`),
  CONSTRAINT `patients_ibfk_1` FOREIGN KEY (`UserID`) REFERENCES `users` (`UserID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (1,2,'Mac','diby','1960-07-26','Male','9722170322','pop','pop'),(2,9,'Joshua','Poll','1997-04-08','Male','6547893210','Josh@','Josh@'),(3,11,'Carl','polll','2004-04-04','Female','98877','dosds','polll@');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `UserID` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(50) NOT NULL,
  `PasswordHash` varbinary(64) DEFAULT NULL,
  `Role` enum('Patient','Doctor') NOT NULL,
  PRIMARY KEY (`UserID`),
  UNIQUE KEY `Username` (`Username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'mdiby',_binary '÷x\à2TCF~‡\î\è‡7-b‡ú€©\"ö\Âù½= /C\È0N;>*P]8ß¼°\Ê\ZMˆa™\ï‰Ivù\Åð\á0\r¾>\É\è¦-','Patient'),(4,'godfrey',_binary 'ÔŸ‚ü`¡H\Ë@ca§N\Þ\á\Îãœ‹\èÁ—Uù\ró\îpLðœ\æ2ø,\Ëh#ƒv\Ù+”œÐ³ˆŸŸ-øu§\Úr³‘','Doctor'),(5,'abena',_binary 'ÿ÷X@“PÕªL”Tµ\Ý$\äkƒ‰2‰³À\Ç;\Z¡ý1t\Zå°t\í¸\ã\ÂC\Ö û\ÌY•.\Û\Ò8BùDQO','Doctor'),(6,'Linco',_binary 'Ø³ký,’¯\0‚µ¾\ÜkJ[\Ú°o\Û;‡·¶\Ó8EýB§qe“\æ‰öŸ;ž\'\Ç|$tJ© bº\ÎøVs$\ã','Doctor'),(7,'Liam',_binary '}\ÄLEx‹²D¬˜º”Nƒ¿‚p.k\×¤g\Ö\"À|\âë¥†™\ëö…¸¿~ÚŠQõMT\á–ÊlG™8C?','Doctor'),(8,'Benj',_binary '‹¦µ¥eb¼L÷¼²\ÌE\å\Ö\Ä;ˆJ\rò\àc\Ïz´Ï«tsÜ©\Çâ¨Œ\áz\è5{¦6 F/Šn E©–¸\Ü\ÓO{\'\é¾','Doctor'),(9,'Josh',_binary '²ª\É\\\Ô\çt|IcN¡\î5\\EŒÂ¶\Ï$«µß¨Mk»‘\èðŸ&Ò€N\ëc\ì©lº?¢Ö‘šuô \Íjl\Ö','Patient'),(10,'paul',_binary 'i2®\×\Þ¶\ÅÑ£¦ª>\n\É|µ\'$3\Ëó¼\ß=\"ÿ\Þz8A1r5¤÷IiN\\\0N¾\"I%‘Õ‰KO«S	’‰¨\ÍÍ„x','Doctor'),(11,'carl',_binary '_\Ègh\Ë¦…K\Öz…”e”?lõXÿV\Ç1A|hG(¼iƒŠ“¡\Ò\"9Ç»\áù\ÑÂ‹\'ùð\Æo!òÐ£l\É\È','Patient');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-09 18:47:59
