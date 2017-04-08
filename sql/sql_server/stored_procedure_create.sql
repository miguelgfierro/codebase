---
--- Create a stored procedure with input and output variables
---

USE [database_name]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

IF OBJECT_ID('[dbo].[StoredProcedureName]', 'P') IS NOT NULL
    DROP PROCEDURE [dbo].[StoredProcedureName];
GO

CREATE PROCEDURE [dbo].[StoredProcedureName]
@VariableInput INT,
@VariableOutput FLOAT OUTPUT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    SELECT @VariableOutput = database_name
    FROM table_name
    WHERE column_name = @VariableInput

	PRINT 'Output:'
	PRINT @VariableOutput
	SELECT @VariableOutput
END
GO



