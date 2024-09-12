-- Script para crear la base de datos y las tablas necesarias

CREATE DATABASE IF NOT EXISTS patient_database;

USE patient_database;

-- Tabla para almacenar la información de los pacientes
CREATE TABLE IF NOT EXISTS patients (
    FULL_NAME VARCHAR(100),
    DOCUMENT VARCHAR(50) PRIMARY KEY,
    DATE_OF_BIRD DATE,
    PHONE VARCHAR(20),
    CONTACT_NAME VARCHAR(100),
    CONTACT_PHONE VARCHAR(20),
    ADDRESS VARCHAR(255),
    EPS VARCHAR(100),
    CIE10 VARCHAR(10),
    MEDICAL_SPECIALTY VARCHAR(100)
);

-- Tabla para almacenar la lista de estudiantes
CREATE TABLE IF NOT EXISTS specialties (
    SPECIALTY_NAME VARCHAR(100),
    DOCUMENT VARCHAR(50) PRIMARY KEY,
    PHONE_1 VARCHAR(20),
    PHONE_2 VARCHAR(20),
    EMAIL VARCHAR(100),
    MEDICAL_SPECIALTY VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS combined_table (
    FULL_NAME VARCHAR(100),
    DOCUMENT VARCHAR(50) PRIMARY KEY,
    PHONE VARCHAR(20),
    EMAIL VARCHAR(100),
    DATE_OF_BIRD DATE,
    CONTACT_NAME VARCHAR(100),
    CONTACT_PHONE VARCHAR(20),
    ADDRESS TEXT,
    EPS VARCHAR(100),
    CIE10 VARCHAR(10),
    SPECIALTY_NAME VARCHAR(100),
    MEDICAL_SPECIALTY VARCHAR(100)
    SPECIALTY_PHONE VARCHAR(20),
);
