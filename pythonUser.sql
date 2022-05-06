-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        10.7.3-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- java_junil 데이터베이스 구조 내보내기
DROP DATABASE IF EXISTS `java_junil`;
CREATE DATABASE IF NOT EXISTS `java_junil` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;
USE `java_junil`;

-- 테이블 java_junil.user_dtl 구조 내보내기
DROP TABLE IF EXISTS `user_dtl`;
CREATE TABLE IF NOT EXISTS `user_dtl` (
  `usercode` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `gender` int(11) DEFAULT NULL,
  `create_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  PRIMARY KEY (`usercode`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 java_junil.user_dtl:~2 rows (대략적) 내보내기
DELETE FROM `user_dtl`;
/*!40000 ALTER TABLE `user_dtl` DISABLE KEYS */;
INSERT INTO `user_dtl` (`usercode`, `address`, `phone`, `gender`, `create_date`, `update_date`) VALUES
	(6, '부산 동래구 사직동', '010-9988-1916', 1, '2022-05-02 20:40:06', '2022-05-02 20:40:06'),
	(7, '부산 동래구 명륜동', '010-9988-1917', 2, '2022-05-02 20:40:06', '2022-05-02 20:40:06');
/*!40000 ALTER TABLE `user_dtl` ENABLE KEYS */;

-- 테이블 java_junil.user_mst 구조 내보내기
DROP TABLE IF EXISTS `user_mst`;
CREATE TABLE IF NOT EXISTS `user_mst` (
  `usercode` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `create_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  PRIMARY KEY (`usercode`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 java_junil.user_mst:~3 rows (대략적) 내보내기
DELETE FROM `user_mst`;
/*!40000 ALTER TABLE `user_mst` DISABLE KEYS */;
INSERT INTO `user_mst` (`usercode`, `email`, `name`, `username`, `password`, `create_date`, `update_date`) VALUES
	(6, 'c@gmail.com', '김준일', 'ccc', '1234', '2022-05-02 20:40:06', '2022-05-02 20:40:06'),
	(7, 'd@gmail.com', '김준일', 'ddd', '1234', '2022-05-02 20:40:06', '2022-05-02 20:40:06');
/*!40000 ALTER TABLE `user_mst` ENABLE KEYS */;

-- 트리거 java_junil.user_mst_after_insert 구조 내보내기
DROP TRIGGER IF EXISTS `user_mst_after_insert`;
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `user_mst_after_insert` AFTER INSERT ON `user_mst` FOR EACH ROW BEGIN
	INSERT into
		user_dtl(
			usercode,
			CREATE_date,
			update_date
		)
	VALUES(
		NEW.usercode,
		NOW(),
		NOW()
	);
		
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

-- 트리거 java_junil.user_mst_before_delete 구조 내보내기
DROP TRIGGER IF EXISTS `user_mst_before_delete`;
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `user_mst_before_delete` BEFORE DELETE ON `user_mst` FOR EACH ROW BEGIN
	delete
	from
		user_dtl
	where
		usercode = OLD.usercode;
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
