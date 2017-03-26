--
-- Script to change the default locations to save the database files
--

USE [master]
GO
 
-- Change default location for data files
EXEC   xp_instance_regwrite
       N'HKEY_LOCAL_MACHINE',
       N'Software\Microsoft\MSSQLServer\MSSQLServer',
       N'DefaultData',
       REG_SZ,
       N'E:\mssql_databases'
GO
 
-- Change default location for log files
EXEC   xp_instance_regwrite
       N'HKEY_LOCAL_MACHINE',
       N'Software\Microsoft\MSSQLServer\MSSQLServer',
       N'DefaultLog',
       REG_SZ,
       N'E:\mssql_databases\logs'
GO
 
-- Change default location for backups
EXEC   xp_instance_regwrite
       N'HKEY_LOCAL_MACHINE',
       N'Software\Microsoft\MSSQLServer\MSSQLServer',
       N'BackupDirectory',
       REG_SZ,
       N'E:\mssql_databases\backup'
GO