-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 05, 2024 at 02:54 PM
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
-- Database: `paulsam_device_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `all_staff`
--

CREATE TABLE `all_staff` (
  `userid` int(20) NOT NULL,
  `check_no` varchar(5) NOT NULL,
  `first_name` varchar(12) NOT NULL,
  `middle_name` varchar(50) NOT NULL,
  `last_name` varchar(10) NOT NULL,
  `title` varchar(10) NOT NULL,
  `gender` varchar(12) NOT NULL,
  `work_station` varchar(15) NOT NULL,
  `department` varchar(22) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `assigned`
--

CREATE TABLE `assigned` (
  `assigned_id` int(50) NOT NULL,
  `assigned_useid` int(20) NOT NULL,
  `assigned_deviceid` int(11) NOT NULL,
  `device_condion` varchar(255) NOT NULL DEFAULT 'working',
  `assigned_time` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `assigned_status` enum('prosess..','complete') NOT NULL DEFAULT 'complete'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `devices`
--

CREATE TABLE `devices` (
  `id` int(55) NOT NULL,
  `deviceid` int(50) NOT NULL,
  `serial_no` varchar(255) NOT NULL,
  `hdd` varchar(255) NOT NULL,
  `ram` varchar(255) NOT NULL,
  `device_model` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `device_name` varchar(255) NOT NULL,
  `os` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `device_condition` varchar(11) NOT NULL,
  `date` timestamp(3) NOT NULL DEFAULT current_timestamp(3) ON UPDATE current_timestamp(3),
  `status` enum('free','used','handover','handover process') NOT NULL,
  `userid` int(50) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `handover`
--

CREATE TABLE `handover` (
  `handover_id` int(50) NOT NULL,
  `handover_useid` int(20) NOT NULL,
  `handover_deviceid` int(11) NOT NULL,
  `handover_reason` varchar(100) NOT NULL,
  `user_file` varchar(255) NOT NULL,
  `handover_time` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `handover_status` enum('non','prosess..','complete') NOT NULL,
  `phone` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `call_id` int(25) NOT NULL,
  `call_userid` int(20) NOT NULL,
  `call_reason` varchar(50) NOT NULL,
  `location` varchar(255) NOT NULL,
  `phone` int(15) NOT NULL,
  `calltime` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `call_status` enum('processed..','complete') NOT NULL DEFAULT 'processed..'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Employee_Number` int(11) NOT NULL,
  `password` varchar(11) NOT NULL,
  `type` enum('user','admn') NOT NULL DEFAULT 'user'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `all_staff`
--
ALTER TABLE `all_staff`
  ADD PRIMARY KEY (`userid`),
  ADD KEY `check_no` (`check_no`);

--
-- Indexes for table `assigned`
--
ALTER TABLE `assigned`
  ADD PRIMARY KEY (`assigned_id`),
  ADD KEY `assigned_deviceid` (`assigned_deviceid`),
  ADD KEY `assigned_useid` (`assigned_useid`);

--
-- Indexes for table `devices`
--
ALTER TABLE `devices`
  ADD PRIMARY KEY (`deviceid`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `userid` (`userid`);

--
-- Indexes for table `handover`
--
ALTER TABLE `handover`
  ADD PRIMARY KEY (`handover_id`),
  ADD KEY `handover_deviceid` (`handover_deviceid`),
  ADD KEY `handover_useid` (`handover_useid`);

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`call_id`),
  ADD KEY `call_userid` (`call_userid`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`Employee_Number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `assigned`
--
ALTER TABLE `assigned`
  MODIFY `assigned_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `devices`
--
ALTER TABLE `devices`
  MODIFY `id` int(55) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- AUTO_INCREMENT for table `handover`
--
ALTER TABLE `handover`
  MODIFY `handover_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `call_id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `assigned`
--
ALTER TABLE `assigned`
  ADD CONSTRAINT `assigned_ibfk_1` FOREIGN KEY (`assigned_useid`) REFERENCES `paulsam`.`authenticationi.t` (`Login_id`);

--
-- Constraints for table `devices`
--
ALTER TABLE `devices`
  ADD CONSTRAINT `devices_ibfk_1` FOREIGN KEY (`id`) REFERENCES `paulsam`.`authenticationi.t` (`Login_id`);

--
-- Constraints for table `handover`
--
ALTER TABLE `handover`
  ADD CONSTRAINT `handover_ibfk_1` FOREIGN KEY (`handover_useid`) REFERENCES `paulsam`.`authenticationi.t` (`Login_id`);

--
-- Constraints for table `request`
--
ALTER TABLE `request`
  ADD CONSTRAINT `request_ibfk_1` FOREIGN KEY (`call_userid`) REFERENCES `paulsam`.`authenticationi.t` (`Login_id`);

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_ibfk_1` FOREIGN KEY (`Employee_Number`) REFERENCES `paulsam`.`authenticationi.t` (`Login_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
