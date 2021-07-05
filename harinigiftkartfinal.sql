-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 03, 2021 at 05:35 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `harinigiftkartfinal`
--

-- --------------------------------------------------------

--
-- Table structure for table `logindetails`
--

CREATE TABLE `logindetails` (
  `UID` int(10) NOT NULL,
  `UserName` varchar(100) NOT NULL,
  `PWD` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `logindetails`
--

INSERT INTO `logindetails` (`UID`, `UserName`, `PWD`) VALUES
(1, 'harini', 'computer'),
(2, 'shop', 'gifts'),
(3, 'alphabear', 'awesomeness'),
(4, 'github', 'sourcecontrol'),
(5, 'sql', 'database');

-- --------------------------------------------------------

--
-- Table structure for table `mailserver`
--

CREATE TABLE `mailserver` (
  `Email` varchar(50) NOT NULL,
  `Pwd` varchar(50) NOT NULL,
  `smtp` varchar(50) NOT NULL,
  `port` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `mailserver`
--

INSERT INTO `mailserver` (`Email`, `Pwd`, `smtp`, `port`) VALUES
('harinigiftskart@gmail.com', 'ics3u1Comp', 'smtp.gmail.com', 587);

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `PID` int(100) NOT NULL,
  `ProductName` varchar(100) NOT NULL,
  `Qty` int(100) NOT NULL,
  `Cost` float NOT NULL,
  `Threshold` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`PID`, `ProductName`, `Qty`, `Cost`, `Threshold`) VALUES
(1, 'Paper Lanterns', 9, 20, 10),
(2, 'Kids Vintage Socks', 10, 2, 5),
(3, 'Stainless Steel Tumler', 100, 10, 5);

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `Trans_ID` int(10) NOT NULL,
  `ProductName` varchar(100) NOT NULL,
  `Qty` int(10) NOT NULL,
  `Amount` float NOT NULL,
  `InvDate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`Trans_ID`, `ProductName`, `Qty`, `Amount`, `InvDate`) VALUES
(1, 'Paper Lanterns', 1, 20, '2021-04-02'),
(2, 'Paper Lanterns', 1, 20, '2021-04-02'),
(3, 'Paper Lanterns', 4, 85, '2021-04-02'),
(4, 'Paper Lanterns', 7, 149, '2021-04-02'),
(5, 'Paper Lanterns', 6, 128, '2021-04-02'),
(6, 'Paper Lanterns', 8, 160, '2021-04-02');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`Trans_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `Trans_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
