// Attribution: https://codepen.io/donovanh/pen/pJzwEw

/* Learn how to create this and much more with this email course:

https://cssanimation.rocks/courses/animation-101/

MANY THANKS TO @tadywankenobi for the following JS to handle the text in the byline:

The following JS takes in the byline and splits it into letters, each one wrapped in a span. We need to create the spans as nodes, we can't just add them to the HTML using innerHTML, as to do so would mean the CSS won't affect the span because it doesn't recognise the tag as existing. It's an old problem we run into time and again.

*/

var byline = document.getElementById('byline');  	// Find the H2
bylineText = byline.innerHTML;										// Get the content of the H2
bylineArr = bylineText.split('');									// Split content into array
byline.innerHTML = '';														// Empty current content

var span;					// Create variables to create elements
var letter;

for (i = 0; i < bylineArr.length; i++) {									// Loop for every letter
    span = document.createElement("span");					// Create a <span> element
    letter = document.createTextNode(bylineArr[i]);	// Create the letter
    if (bylineArr[i] == ' ') {												// If the letter is a space...
        byline.appendChild(letter);					// ...Add the space without a span
    } else {
        span.appendChild(letter);						// Add the letter to the span
        byline.appendChild(span); 					// Add the span to the h2
    }
}

