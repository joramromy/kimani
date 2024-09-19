-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 05, 2024 at 02:53 PM
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
-- Database: `kimani_stores`
--

-- --------------------------------------------------------

--
-- Table structure for table `authenticationprocurement`
--

CREATE TABLE `authenticationprocurement` (
  `Login_id` int(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `full_name` varchar(20) NOT NULL,
  `age` varchar(250) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `Phone` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `comfirm_password` varchar(50) NOT NULL,
  `reset_token` varchar(255) NOT NULL,
  `token_expiry` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `authenticationprocurement`
--

INSERT INTO `authenticationprocurement` (`Login_id`, `username`, `full_name`, `age`, `gender`, `Phone`, `email`, `Password`, `comfirm_password`, `reset_token`, `token_expiry`) VALUES
(1, 'joram', 'joram gwamaka', '', 'Male', 678721526, 'joramgwamaka@gmail.com', 'romezinho10', 'romezinho10', '', '2024-07-31 11:32:45');

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

--
-- Dumping data for table `user_progress`
--

INSERT INTO `user_progress` (`user_id`, `address_completed`, `customer_completed`, `kin_completed`, `userpage_completed`, `Add_goal_completed`, `New_goal_completed`, `usser_id`) VALUES
(1, 0, 0, 0, 0, 0, 0, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authenticationprocurement`
--
ALTER TABLE `authenticationprocurement`
  ADD PRIMARY KEY (`Login_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authenticationprocurement`
--
ALTER TABLE `authenticationprocurement`
  MODIFY `Login_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
