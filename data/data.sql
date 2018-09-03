-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 03, 2018 at 05:31 PM
-- Server version: 5.7.23-0ubuntu0.18.04.1
-- PHP Version: 7.2.7-0ubuntu0.18.04.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gotit`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `email` varchar(50) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `facebook_id` varchar(50) DEFAULT NULL,
  `google_id` varchar(50) DEFAULT NULL,
  `status` int(1) DEFAULT NULL,
  `type` int(1) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `labor` int(2) DEFAULT NULL,
  `note` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`email`, `name`, `facebook_id`, `google_id`, `status`, `type`, `phone`, `labor`, `note`) VALUES
('thdang1003@gmail.com', 'Tran Dang', '100006088690251', NULL, 1, 0, '0168132798', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `id_post` int(11) NOT NULL,
  `title` text NOT NULL,
  `main` text NOT NULL,
  `post_by` varchar(50) NOT NULL,
  `count_liked` int(11) NOT NULL,
  `note` varchar(100) NOT NULL,
  `email_like` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`id_post`, `title`, `main`, `post_by`, `count_liked`, `note`, `email_like`) VALUES
(1, 'Hello World', 'After your application obtains an access token, you can use the token to make calls to a Google API on behalf of a given user account or service account. To do this, include the access token in a request to the API by including either an access_token query parameter or an Authorization: Bearer HTTP header. When possible, the HTTP header is preferable, because query strings tend to be visible in server logs. In most cases you can use a client library to set up your calls to Google APIs ', 'thdang1003@gmail.com', 3, 'After your application obtains an access token, you can use the token to make calls to a G', NULL),
(2, 'Hello World_1', 'trần hăi đăng After your application obtains an access token, you can use the token to make calls to a Google API on behalf of a given user account or service account. To do this, include the access token in a request to the API by including either an access_token query parameter or an Authorization: Bearer HTTP header. When possible, the HTTP header is preferable, because query strings tend to be visible in server logs. In most cases you can use a client library to set up your calls to Google APIs ', 'thdang1003@gmail.com', 0, 'trần hăi đăng After your application obtains an access token, you can use the token to mak', NULL),
(3, 'Hello World_2', 'trần hăi đăng After your application obtains an access token, you can use the token to make calls to a Google API on behalf of a given user account or service account. To do this, include the access token in a request to the API by including either an access_token query parameter or an Authorization: Bearer HTTP header. When possible, the HTTP header is preferable, because query strings tend to be visible in server logs. In most ', 'thdang1003@gmail.com', 0, 'trần hăi đăng After your application obtains an access token, you can use the token to mak', NULL),
(4, 'Hello World_3', 'trần hăi đăng After your application obtains an access token, you can use the token to make calls to a Google API on behalf of a given user account or service account. To do this, include the access token in a request to the API by including either an access_token query parameter or an Authorization: Bearer HTTP header. When possible, the HTTP header is preferable, because query strings tend to be visible in server logs. In most ', 'thdang1003@gmail.com', 0, 'trần hăi đăng After your application obtains an access token, you can use the token to mak', NULL),
(5, 'Hello World_4', 'trần hăi đăng After your application obtains an access token, you can use the token to make calls to a Google API on behalf of a given user account or service account. To do this, include the access token in a request to the API by including either an access_token query parameter or an Authorization: Bearer HTTP header. When possible, the HTTP header is preferable, because query strings tend to be visible in server logs. In most ', 'thdang1003@gmail.com', 0, 'trần hăi đăng After your application obtains an access token, you can use the token to mak', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `post_liked`
--

CREATE TABLE `post_liked` (
  `id` int(11) NOT NULL,
  `id_post` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `post_liked`
--

INSERT INTO `post_liked` (`id`, `id_post`, `email`) VALUES
(1, '1', 'thdang1003@gmail.com'),
(2, '1', 'thdang1003@gmail.com'),
(3, '1', 'thdang1003@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`id_post`);

--
-- Indexes for table `post_liked`
--
ALTER TABLE `post_liked`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `id_post` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `post_liked`
--
ALTER TABLE `post_liked`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;