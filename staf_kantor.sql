-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 12, 2024 at 01:29 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kantor_kampus`
--

-- --------------------------------------------------------

--
-- Table structure for table `staf_kantor`
--

CREATE TABLE `staf_kantor` (
  `id` int(10) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `agama` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `staf_kantor`
--

INSERT INTO `staf_kantor` (`id`, `nama`, `agama`) VALUES
(2222, 'zul', 'protestan'),
(2314, 'alif', 'islam'),
(3453, 'kilo', 'kristen'),
(5555, 'hhhh', 'ooooo'),
(6590, 'budha', 'aril'),
(8780, 'kristen', 'riflan');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `staf_kantor`
--
ALTER TABLE `staf_kantor`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
