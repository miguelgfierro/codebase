var fs = require("fs");


/**
 * Save an array to a file (separated by commas)
 * @param {Array} data - Array.
 * @param {String} filename - Name of the file.
 */
function saveFile(data, filename){
    var dataStr = '';
    for(i=0;i<data.length;i++){
        dataStr += data[i].toString() + '\n';
    }
    fs.writeFile(filename, dataStr, function(err, data){
        if (err) console.log("ERROR: " + err);
    });
}


/**
 * Read a csv file (separated by commas)
 * @param {String} filename - Name of the file.
 * @return {Array} - Array with the elements.
 */
function readFile(filename){
    var items = [];
    var fileContents = fs.readFileSync(filename);
    var lines = fileContents.toString().split('\n');

    for (var i = 0; i < lines.length; i++) {
        if (lines[i] != ''){
            items.push(lines[i].toString().split(','));
        }
    }
    return items;
}


/**
 * Test with mocha. To run the test, in a terminal type:
 * mocha
 */

var assert = require('assert');

describe('test saveFile', function() {
    it('save values and make sure they are correct', function() {
        data = [
        [1,2,3],
        [4,5,6]
        ];
        saveFile(data, 'file.csv');
        items = readFile('file.csv');
        assert.deepEqual(['1','2','3'], items[0]);
        assert.deepEqual(['4','5','6'], items[1]);
    });
});


describe('test readFile', function() {
    it('should return the values in traj.csv', function() {
        items = readFile("../../share/traj.csv");
        assert.deepEqual(['0.0416667','443','205'], items[0]);
        assert.deepEqual(['0.0833333','444','206'], items[1]);
    });
});




