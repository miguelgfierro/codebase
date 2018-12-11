<?php
    /*
    Write a txt file
    
    $ php write_txt.php 
    */
    $filename = "file.txt";
    $file = fopen( $filename, "w" );

    if( $file == false ) {
        echo ( "Error in opening new file" );
        exit();
    }
    fwrite( $file, "This is a simple test\n" );
    fclose( $file );
?>