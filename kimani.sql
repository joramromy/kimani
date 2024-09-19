-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 05, 2024 at 02:46 PM
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
-- Database: `kimani`
--

-- --------------------------------------------------------

--
-- Table structure for table `attachments`
--

CREATE TABLE `attachments` (
  `id` int(11) NOT NULL,
  `message_id` int(11) DEFAULT NULL,
  `file_path` varchar(255) DEFAULT NULL,
  `file_type` enum('photo','video') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `authentication`
--

CREATE TABLE `authentication` (
  `Login_id` int(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `full_name` varchar(200) NOT NULL,
  `age` varchar(200) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `Phone` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `comfirm_password` varchar(50) NOT NULL,
  `reset_token` varchar(255) NOT NULL,
  `token_expiry` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `authentication`
--

INSERT INTO `authentication` (`Login_id`, `username`, `full_name`, `age`, `gender`, `Phone`, `email`, `Password`, `comfirm_password`, `reset_token`, `token_expiry`) VALUES
(2, 'joram', 'joram gwamaka', '1990-11-10', 'Male', 678721526, 'joramgwamak@gmail.com', 'romezinho', 'romezinho10', 'so0SbuaucH', '2024-07-25 17:48:27');

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

--
-- Dumping data for table `authenticationadmin`
--

INSERT INTO `authenticationadmin` (`Login_id`, `username`, `full_name`, `age`, `gender`, `Phone`, `email`, `rank`, `Password`, `comfirm_password`, `reset_token`, `token_expiry`) VALUES
(2, 'joram', 'joram gwamaka', '', 'Male', 678721526, 'joramgwamaka@gmail.com', 'i.t', 'romezinho', 'romezinho10', 'GLgmzmh5gk', '2024-07-25 16:10:52');

-- --------------------------------------------------------

--
-- Table structure for table `groups`
--

CREATE TABLE `groups` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `sender` varchar(255) NOT NULL,
  `message` text DEFAULT NULL,
  `attachment_path` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
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

--
-- Dumping data for table `user_progress`
--

INSERT INTO `user_progress` (`user_id`, `address_completed`, `customer_completed`, `kin_completed`, `userpage_completed`, `Add_goal_completed`, `New_goal_completed`, `usser_id`) VALUES
(2, 0, 0, 0, 0, 0, 0, NULL),
(0, 0, 0, 0, 0, 0, 0, NULL),
(2, 0, 0, 0, 0, 0, 0, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attachments`
--
ALTER TABLE `attachments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `message_id` (`message_id`);

--
-- Indexes for table `authentication`
--
ALTER TABLE `authentication`
  ADD PRIMARY KEY (`Login_id`);

--
-- Indexes for table `authenticationadmin`
--
ALTER TABLE `authenticationadmin`
  ADD PRIMARY KEY (`Login_id`);

--
-- Indexes for table `groups`
--
ALTER TABLE `groups`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `group_id` (`group_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attachments`
--
ALTER TABLE `attachments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `authentication`
--
ALTER TABLE `authentication`
  MODIFY `Login_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `authenticationadmin`
--
ALTER TABLE `authenticationadmin`
  MODIFY `Login_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `groups`
--
ALTER TABLE `groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attachments`
--
ALTER TABLE `attachments`
  ADD CONSTRAINT `attachments_ibfk_1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`);

--
-- Constraints for table `messages`
--
ALTER TABLE `messages`
  ADD CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
