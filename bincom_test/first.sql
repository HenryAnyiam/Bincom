-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 20, 2011 at 05:08 PM
-- Server version: 5.1.36
-- PHP Version: 5.2.9-2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `bincomphptest`
--
DROP DATABASE IF EXISTS `bincomphptest`;
CREATE DATABASE IF NOT EXISTS `bincomphptest`;

-- --------------------------------------------------------

-- User: `bincom`
CREATE USER IF NOT EXISTS 'bincom'@'localhost' IDENTIFIED BY 'bincom_pwd';
GRANT ALL ON `bincomphptest`.* TO 'bincom'@'localhost';
GRANT SELECT ON performance_schema.* TO 'bincom'@'localhost';
