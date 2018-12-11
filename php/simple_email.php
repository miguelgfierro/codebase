<?php
/* Send a simple email.

To execute this, first make sure you have an apache server and php installed, 
then execute:
$ php my_file.php

source: https://www.w3schools.com/php/func_mail_mail.asp
NOTE: this will probably go to the spam folder.
*/

// the message
$msg = "First line of text\nSecond line of text";

// use wordwrap() if lines are longer than 70 characters
$msg = wordwrap($msg,70);

// send email
mail("hoaphumanoid@gmail.com","My subject",$msg);
?> 