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
-- Database: `kimani_drilling`
--

-- --------------------------------------------------------

--
-- Table structure for table `authenticationdrilling`
--

CREATE TABLE `authenticationdrilling` (
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
-- Dumping data for table `authenticationdrilling`
--

INSERT INTO `authenticationdrilling` (`Login_id`, `username`, `full_name`, `age`, `gender`, `Phone`, `email`, `Password`, `comfirm_password`, `reset_token`, `token_expiry`) VALUES
(1, 'joram', 'joram gwamaka', '', 'Male', 678721526, 'joramgwamaka@gmail.com', 'romezinho10', 'romezinho10', '', '2024-07-31 14:28:51');

-- --------------------------------------------------------

--
-- Table structure for table `drilling_reports`
--

CREATE TABLE `drilling_reports` (
  `report_id` int(250) NOT NULL,
  `Date` varchar(200) NOT NULL,
  `Depth_started` varchar(255) NOT NULL,
  `Depth_ended` varchar(255) NOT NULL,
  `Total_meter_drilled` varchar(250) NOT NULL,
  `Hole_id` varchar(250) NOT NULL,
  `Drilling_angle` varchar(250) NOT NULL,
  `Drilling_bit_type` varchar(250) NOT NULL,
  `Login_id` int(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `drilling_reports`
--

INSERT INTO `drilling_reports` (`report_id`, `Date`, `Depth_started`, `Depth_ended`, `Total_meter_drilled`, `Hole_id`, `Drilling_angle`, `Drilling_bit_type`, `Login_id`) VALUES
(1, '2024-07-31', '54', '25', '16', 'hsifhiow', '50', 'mn', NULL),
(2, '2024-07-31', '42.4m', '54.3m', '12m', 'MDH08', '50', 'HQ3', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `drilling_reports_night_shift`
--

CREATE TABLE `drilling_reports_night_shift` (
  `report_id` int(250) NOT NULL,
  `Date` varchar(200) NOT NULL,
  `Depth_started` varchar(255) NOT NULL,
  `Depth_ended` varchar(255) NOT NULL,
  `Total_meter_drilled` varchar(250) NOT NULL,
  `Hole_id` varchar(250) NOT NULL,
  `Drilling_angle` varchar(250) NOT NULL,
  `Drilling_bit_type` varchar(250) NOT NULL,
  `Login_id` int(200) NOT NULL
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
(1, 0, 0, 0, 0, 0, 0, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `authenticationdrilling`
--
ALTER TABLE `authenticationdrilling`
  ADD PRIMARY KEY (`Login_id`);

--
-- Indexes for table `drilling_reports`
--
ALTER TABLE `drilling_reports`
  ADD PRIMARY KEY (`report_id`),
  ADD KEY `Login_id` (`Login_id`);

--
-- Indexes for table `drilling_reports_night_shift`
--
ALTER TABLE `drilling_reports_night_shift`
  ADD PRIMARY KEY (`report_id`),
  ADD KEY `Login_id` (`Login_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `authenticationdrilling`
--
ALTER TABLE `authenticationdrilling`
  MODIFY `Login_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `drilling_reports`
--
ALTER TABLE `drilling_reports`
  MODIFY `report_id` int(250) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `drilling_reports_night_shift`
--
ALTER TABLE `drilling_reports_night_shift`
  MODIFY `report_id` int(250) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `drilling_reports`
--
ALTER TABLE `drilling_reports`
  ADD CONSTRAINT `drilling_reports_ibfk_1` FOREIGN KEY (`Login_id`) REFERENCES `authenticationdrilling` (`Login_id`);

--
-- Constraints for table `drilling_reports_night_shift`
--
ALTER TABLE `drilling_reports_night_shift`
  ADD CONSTRAINT `drilling_reports_night_shift_ibfk_1` FOREIGN KEY (`Login_id`) REFERENCES `drilling_reports` (`Login_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
