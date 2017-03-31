--
-- Enable external scripts like R or python.
-- More info:
-- https://docs.microsoft.com/en-us/sql/advanced-analytics/r-services/set-up-sql-server-r-services-in-database
--
-- NOTE: After executing the script you have to restart the server (MSSQLSERVER Launchpad in services)
-- for this to work. To ensure that the service is activated run_value has to be set to 1.
--

-- See SQL Server configuration
sp_configure

-- Enable external scripts
Exec sp_configure 'external scripts enabled', 1
Reconfigure with override

