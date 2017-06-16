/**
 * Replace a string pattern with another
 * @param {String} data - The string to be cleaned
 * @param {String} string_to_clean - Character or group of characters to clean
 * @param {String} string_to_replace - Character or group of characters replacing the string_to_clean
 * @return {String} - The string cleaned
 */
function cleanString(data, string_to_clean, string_to_replace){
	var regex = new RegExp(string_to_clean, 'g');
	data = data.trim();
	data = data.replace(regex, string_to_replace);
	return data;
}
