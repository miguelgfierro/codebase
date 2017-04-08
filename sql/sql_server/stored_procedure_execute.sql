---
--- Execute the stored procedure created in file stored_procedure_create.sql
---

DECLARE @VariableOutputSP FLOAT;
EXECUTE dbo.StoredProcedureName @VariableInput = 0, @VariableOutput = @VariableOutputSP;
