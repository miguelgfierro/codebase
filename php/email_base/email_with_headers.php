<?php
/* Send an email with headers.

To execute this, first make sure you have an apache server and php installed, 
then execute:
$ php my_file.php

source: https://www.w3schools.com/php/func_mail_mail.asp
NOTE: this will probably go to the spam folder.
*/
$to = "hoaphumanoid@gmail.com";
$subject = "My subject";
$txt = "Hello world!";
$headers = "From: webmaster@example.com" . "\r\n" .
"CC: somebodyelse@example.com";

mail($to,$subject,$txt,$headers);
?>