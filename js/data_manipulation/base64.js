// Converts and image or video to base64

// Package: https://www.npmjs.com/package/datauri
// To install: $ npm install --save datauri
// To run: node base64.js

const datauri = require('datauri');

const file = 'path/to/image/i.png'
//const file = 'path/to/video/v.mp4'

datauri(file, (err, content, meta) => {
    if (err) {
        throw err;
    }
    console.log(content)
});
