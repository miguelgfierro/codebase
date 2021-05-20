// To enable this function, I need to create a trigger. Go to Triggers, Add Trigger. Then select the following options:
// Choose which function to run: onSelectionChange 
// Select event source: From spreadsheet
// Select event type: On edit
function onSelectionChange(e) {
  //Logger.log(JSON.stringify(e));
  const as = e.source.getActiveSheet();
  const col = e.range.getColumn();
  // Automatically execute when there is a change in sheet Miguel and column G
  if (as.getName() == 'Miguel' && col === 7){
   rutinaMacros(); 
  }
}

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
      
      // Hidratos
      var cellCH = range.offset(0, 3).getCell(i,1);
      if (cellCH.isBlank()){
        var formulaCH = formula.replace(/Meals!B/g, "Meals!E").replace(/Foods!C/g, "Foods!F");
        //Logger.log(formulaGrasas)
        Logger.log("Computando hidratos en celda %s", cellCH.getA1Notation());
        cellCH.setFormula(formulaCH);
      } 
    }
  }
  Logger.log("Rutina finalizada")

}
