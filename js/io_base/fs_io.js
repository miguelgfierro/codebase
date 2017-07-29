var fs = require("fs");


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
        items.push(lines[i].toString().split(','));
    }
    return items;
}


/**
 * Test with mocha. To run the test, in a terminal type:
 * mocha
 */
var assert = require('assert');
describe('test readFile', function() {
    it('should return the values in traj.csv', function() {
        items = readFile("../../share/traj.csv");
        assert.deepEqual(['0.0416667','443','205'], items[0]);
        assert.deepEqual(['0.0833333','444','206'], items[1]);
    });
});


