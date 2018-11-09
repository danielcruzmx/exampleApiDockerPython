-- phpMyAdmin SQL Dump
-- version 4.7.8
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generacion: 03-11-2018 a las 04:15:26
-- Version del servidor: 5.7.23
-- Version de PHP: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Base de datos: `test`
--
CREATE DATABASE IF NOT EXISTS `test` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `test`;

--
-- Estructura de tabla para la tabla `articulo`
--
CREATE TABLE `articulo` (
  `id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `descripcion` varchar(20) NOT NULL,
  `precio` decimal(12,1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `articulo`
--
INSERT INTO `articulo` (`id`, `cantidad`, `descripcion`, `precio`) VALUES
(1, 5, 'Lapices', '1.5'),
(2, 10, 'Cuadernos', '15.3'),
(3, 1, 'Caja de clips', '10.0'),
(4, 3, 'Caja de colores', '40.0');

--
-- Indices de la tabla `articulo`
--
ALTER TABLE `articulo`
  ADD PRIMARY KEY (`id`);
COMMIT;
