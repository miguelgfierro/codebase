<?php
/* Send a simple email.

source: https://www.w3schools.com/php/func_mail_mail.asp
NOTE: this will probably go to the spam folder, since it doesn't have headers
*/

// the message
$msg = "First line of text\nSecond line of text";

// use wordwrap() if lines are longer than 70 characters
$msg = wordwrap($msg,70);

// send email
mail("hoaphumanoid@gmail.com","My subject",$msg);
?> 