-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 05, 2024 at 02:50 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.4.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kimani_administration`
--

-- --------------------------------------------------------

--
-- Table structure for table `authenticationadmin`
--

CREATE TABLE `authenticationadmin` (
  `Login_id` int(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `full_name` varchar(20) NOT NULL,
  `age` varchar(250) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `Phone` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `rank` varchar(200) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `comfirm_password` varchar(50) NOT NULL,
  `reset_token` varchar(255) NOT NULL,
  `token_expiry` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_progress`
--

CREATE TABLE `user_progress` (
  `user_id` int(200) NOT NULL,
  `address_completed` tinyint(1) NOT NULL,
  `customer_completed` tinyint(1) NOT NULL,
  `kin_completed` tinyint(1) NOT NULL,
  `userpage_completed` tinyint(1) NOT NULL,
  `Add_goal_completed` tinyint(1) NOT NULL,
  `New_goal_completed` tinyint(1) NOT NULL,
  `usser_id` int(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
