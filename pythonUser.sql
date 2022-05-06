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


-- python_junil 데이터베이스 구조 내보내기
DROP DATABASE IF EXISTS `python_junil`;
CREATE DATABASE IF NOT EXISTS `python_junil` /*!40100 DEFAULT CHARACTER SET utf8mb3 */;
USE `python_junil`;

-- 테이블 python_junil.category_mst 구조 내보내기
DROP TABLE IF EXISTS `category_mst`;
CREATE TABLE IF NOT EXISTS `category_mst` (
  `category_code` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(50) NOT NULL,
  `create_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  PRIMARY KEY (`category_code`),
  UNIQUE KEY `category_name` (`category_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 python_junil.category_mst:~3 rows (대략적) 내보내기
DELETE FROM `category_mst`;
/*!40000 ALTER TABLE `category_mst` DISABLE KEYS */;
INSERT INTO `category_mst` (`category_code`, `category_name`, `create_date`, `update_date`) VALUES
	(1, '텀블러', '2022-05-03 19:43:29', '2022-05-03 19:43:29'),
	(2, '머그컵', '2022-05-03 19:43:29', '2022-05-03 19:43:29'),
	(3, '커피', '2022-05-03 19:43:29', '2022-05-03 19:43:29');
/*!40000 ALTER TABLE `category_mst` ENABLE KEYS */;

-- 테이블 python_junil.itemcode_mst 구조 내보내기
DROP TABLE IF EXISTS `itemcode_mst`;
CREATE TABLE IF NOT EXISTS `itemcode_mst` (
  `item_code` int(11) NOT NULL DEFAULT 0,
  `item_name` varchar(50) NOT NULL,
  `create_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  PRIMARY KEY (`item_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 python_junil.itemcode_mst:~2 rows (대략적) 내보내기
DELETE FROM `itemcode_mst`;
/*!40000 ALTER TABLE `itemcode_mst` DISABLE KEYS */;
INSERT INTO `itemcode_mst` (`item_code`, `item_name`, `create_date`, `update_date`) VALUES
	(1, '남성', '2022-05-03 20:52:50', '2022-05-03 20:52:51'),
	(2, '여성', '2022-05-03 20:52:58', '2022-05-03 20:52:59');
/*!40000 ALTER TABLE `itemcode_mst` ENABLE KEYS */;

-- 테이블 python_junil.product_mst 구조 내보내기
DROP TABLE IF EXISTS `product_mst`;
CREATE TABLE IF NOT EXISTS `product_mst` (
  `product_code` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) NOT NULL,
  `category_code` int(11) NOT NULL,
  `create_date` datetime NOT NULL,
  `update_date` datetime NOT NULL,
  PRIMARY KEY (`product_code`),
  UNIQUE KEY `product_name` (`product_name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 python_junil.product_mst:~6 rows (대략적) 내보내기
DELETE FROM `product_mst`;
/*!40000 ALTER TABLE `product_mst` DISABLE KEYS */;
INSERT INTO `product_mst` (`product_code`, `product_name`, `category_code`, `create_date`, `update_date`) VALUES
	(1, '스타벅스 블랙 텀블러', 1, '2022-05-03 19:37:16', '2022-05-03 19:37:16'),
	(2, '스타벅스 레드 텀블러', 1, '2022-05-03 19:37:16', '2022-05-03 19:37:16'),
	(3, '스타벅스 화이트 머그컵', 2, '2022-05-03 19:37:16', '2022-05-03 19:37:16'),
	(4, '스타벅스 레드 머그컵', 2, '2022-05-03 19:37:16', '2022-05-03 19:37:16'),
	(5, '아이스아메리카노', 3, '2022-05-03 19:37:16', '2022-05-03 19:37:16'),
	(6, '에스프레소', 3, '2022-05-03 19:37:16', '2022-05-03 19:37:16'),
	(7, '치즈 셀러드', 4, '2022-05-03 20:07:06', '2022-05-03 20:07:06');
/*!40000 ALTER TABLE `product_mst` ENABLE KEYS */;

-- 테이블 python_junil.user_dtl 구조 내보내기
DROP TABLE IF EXISTS `user_dtl`;
CREATE TABLE IF NOT EXISTS `user_dtl` (
  `usercode` int(11) NOT NULL AUTO_INCREMENT,
  `phone` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `gender` int(11) DEFAULT NULL,
  `introduce` text DEFAULT NULL,
  `createdate` datetime NOT NULL,
  `updatedate` datetime NOT NULL,
  PRIMARY KEY (`usercode`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 python_junil.user_dtl:~3 rows (대략적) 내보내기
DELETE FROM `user_dtl`;
/*!40000 ALTER TABLE `user_dtl` DISABLE KEYS */;
INSERT INTO `user_dtl` (`usercode`, `phone`, `address`, `gender`, `introduce`, `createdate`, `updatedate`) VALUES
	(1, '010-9988-1916', '부산 동래구 사직동', 1, '안녕하세요.\n김준일입니다.', '2022-04-28 21:22:42', '2022-04-28 21:22:42'),
	(2, '010-9988-1234', '부산 부산진구 가야동', 2, '안녕하세요.\n김준이입니다.', '2022-04-28 21:22:42', '2022-04-28 21:22:42'),
	(4, '010-9988-1234', '서울 부산진구 가야동', 2, '안녕하세요.\n김준이입니다.', '2022-04-28 21:30:54', '2022-04-28 21:30:54'),
	(8, NULL, NULL, NULL, NULL, '2022-05-03 21:30:34', '2022-05-03 21:30:34');
/*!40000 ALTER TABLE `user_dtl` ENABLE KEYS */;

-- 테이블 python_junil.user_mst 구조 내보내기
DROP TABLE IF EXISTS `user_mst`;
CREATE TABLE IF NOT EXISTS `user_mst` (
  `usercode` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `createdate` datetime NOT NULL,
  `updatedate` datetime NOT NULL,
  PRIMARY KEY (`usercode`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;

-- 테이블 데이터 python_junil.user_mst:~5 rows (대략적) 내보내기
DELETE FROM `user_mst`;
/*!40000 ALTER TABLE `user_mst` DISABLE KEYS */;
INSERT INTO `user_mst` (`usercode`, `email`, `name`, `username`, `password`, `createdate`, `updatedate`) VALUES
	(1, 'skjil1218@kakao.com', '김준일', 'junil', '1234', '2022-04-28 20:40:03', '2022-04-28 20:40:03'),
	(2, 'ssss@kakao.com', '김준이', 'ss', '1111', '2022-04-28 20:46:08', '2022-04-28 20:46:08'),
	(3, 'aaaa@kakao.com', '김준삼', 'aa', '2222', '2022-04-28 20:50:16', '2022-04-28 20:50:16'),
	(4, 'bbbb@kakao.com', '김준사', 'bb', '3333', '2022-04-28 20:50:16', '2022-04-28 20:50:16'),
	(5, 'cccc@kakao.com', '김준사', 'cc', '4444', '2022-04-28 20:50:16', '2022-04-28 20:50:16'),
	(8, 'aaaa@gmail.com', '김준오', 'junil5', '1234', '2022-05-03 21:30:34', '2022-05-03 21:30:34');
/*!40000 ALTER TABLE `user_mst` ENABLE KEYS */;

-- 트리거 python_junil.user_mst_after_insert 구조 내보내기
DROP TRIGGER IF EXISTS `user_mst_after_insert`;
SET @OLDTMP_SQL_MODE=@@SQL_MODE, SQL_MODE='STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
DELIMITER //
CREATE TRIGGER `user_mst_after_insert` AFTER INSERT ON `user_mst` FOR EACH ROW BEGIN
	INSERT into
		user_dtl(
			usercode,
			createdate,
			updatedate
		)
	VALUES(
		NEW.usercode,
		NOW(),
		NOW()
	);
END//
DELIMITER ;
SET SQL_MODE=@OLDTMP_SQL_MODE;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
