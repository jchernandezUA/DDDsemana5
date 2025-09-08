-- Initialization script for AlpesPartners PostgreSQL database
-- This script will be executed when the PostgreSQL container starts for the first time

-- Create database if it doesn't exist (though it should already exist from POSTGRES_DB)
-- SELECT 'CREATE DATABASE alpespartners' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'alpespartners');

-- Set up any initial configuration or users if needed
-- For now, we'll let SQLAlchemy handle table creation through db.create_all()

-- Grant all privileges to the postgres user (default setup)
GRANT ALL PRIVILEGES ON DATABASE alpespartners TO postgres;

-- Create any additional schemas if needed
-- CREATE SCHEMA IF NOT EXISTS public;

-- You can add any other initialization queries here
