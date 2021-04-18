function rutinaMacros() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName("Miguel");
  var range = sheet.getRange("G156:G250");
  var numRows = range.getNumRows();

  for (i=1; i<=numRows; i++){
    var cell = range.getCell(i,1); //only one column
    Logger.log("Ejecutando celda: %s", cell.getA1Notation())

    if (!cell.isBlank()){
      var formula = cell.getFormula();

      // Proteinas
      var cellProteinas = range.offset(0, 1).getCell(i,1);
      if (cellProteinas.isBlank()){
        var formulaProteinas = formula.replace(/Meals!B/g, "Meals!J").replace(/Foods!C/g, "Foods!K");
        //Logger.log(formulaProteinas)
        Logger.log("Computando proteínas en celda %s", cellProteinas.getA1Notation());
        cellProteinas.setFormula(formulaProteinas);

      }
      
      // Grasas
      var cellGrasas = range.offset(0, 2).getCell(i,1);
      if (cellGrasas.isBlank()){
        var formulaGrasas = formula.replace(/Meals!B/g, "Meals!D").replace(/Foods!C/g, "Foods!E");
        //Logger.log(formulaGrasas)
        Logger.log("Computando grasas en celda %s", cellGrasas.getA1Notation());
        cellGrasas.setFormula(formulaGrasas);
      } 
    }
  }
  Logger.log("Rutina finalizada")

}
