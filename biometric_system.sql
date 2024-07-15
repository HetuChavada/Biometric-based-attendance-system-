-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 29, 2024 at 10:51 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `biometric_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `p_id` int(10) NOT NULL,
  `P_name` varchar(50) NOT NULL,
  `password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `fname` varchar(45) DEFAULT NULL,
  `lname` varchar(45) NOT NULL,
  `contact` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `securityQ` varchar(45) NOT NULL,
  `securityA` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`fname`, `lname`, `contact`, `email`, `securityQ`, `securityA`, `password`) VALUES
('hetal', 'chavda', '9313707011', 'Ayesha03', 'Your birth place', 'rajkot', '123'),
('Hetal', 'chavda', '9313707011', 'hetal03', 'Your birth place', 'rajkot', '@hetal03'),
('Hetal', 'chavda', '9313707011', 'hetal03@gmail.com', 'Your birth place', 'rajkot', '123'),
('hetal', 'chavda', '9313707011', 'hetal06', 'Your birth place', 'rajkot', '123'),
('hetal', 'chavda', '9313707011', 'hetalchavda816@gmail.com', 'Your friend name', 'Raksha', '@hetu'),
('hetal', 'chavda', '9313707011', 'hetalchavda@gmail.com', 'Your friend name', 'nilam', '123'),
('parmar', 'nilam', '230967545', 'parmarnilam@gmail.com', 'Your friend name', 'hetal', '123456'),
('priyal', 'faldu', '9313707011', 'priyal03', 'Your birth place', 'rajkot', '123'),
('shreemanta', 'chauhan', '88978', 'shree03@gmail.com', 'Your birth place', 'rajkot', '@shree');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `Dept` varchar(45) DEFAULT NULL,
  `course` varchar(45) DEFAULT NULL,
  `year` varchar(45) DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  `student_id` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `Division` varchar(45) DEFAULT NULL,
  `Roll` varchar(45) DEFAULT NULL,
  `gender` varchar(45) DEFAULT NULL,
  `dob` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `teacher` varchar(45) DEFAULT NULL,
  `PhotoSample` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`Dept`, `course`, `year`, `semester`, `student_id`, `name`, `Division`, `Roll`, `gender`, `dob`, `email`, `phone`, `address`, `teacher`, `PhotoSample`) VALUES
('IT', 'TE', '2021-22', 'Semester-1', '1', 'hetal', 'A', '1', 'female', '30-03-2003', 'hetalchavda816@gmail.com', '9313707011', 'Delhi', 'david', 'NO');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`p_id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `p_id` int(10) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
