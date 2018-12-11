<?php
    /*
    Read a txt file
    
    $ php read_txt.php 
    */
    $filename = "../../share/traj.txt";
    $file = fopen($filename, "r");
    
    if($file == false) {
        echo ("Error in opening file");
    exit();
    }
    
    $filesize = filesize($filename);
    $filetext = fread($file, $filesize);
    fclose($file);
    
    echo("File size : $filesize bytes");
    echo("\n");
    echo("$filetext \n");
?>