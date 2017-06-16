/**
 * Get current date in the format yyyy-mm-dd HH:mm:ss
 * @return {String} - Date
 */
function getDateFromNow(){
	var date = new Date();
	return date.getFullYear()+'-'+(date.getMonth()<10?'0':'')+(date.getMonth()+1)+'-'+(date.getDate()<10?'0':'')+date.getDate()+' '+(date.getHours()<10?'0':'')+date.getHours()+':'+(date.getMinutes()<10?'0':'')+date.getMinutes()+':'+(date.getSeconds()<10?'0':'')+date.getSeconds();
}
