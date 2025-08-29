# Windows Subsystem for Linux (WSL)


## Installation 

To run the `wsl` command, use a command promp with admin rights.

To list the current distributions:

    wsl -l
    
To list all available distributions:

    wsl -l --online
    
To install one of the default distributions:

    wsl --install

To install one, just add the distribution name:

    wsl --install Ubuntu-20.04

For installing older distributions like Ubuntu 16.04: https://docs.microsoft.com/en-us/windows/wsl/install-manual. Download the file and execute.

## Configure WSL memory

First, close all open WSL-2 and open CMD, enter the following command:

    wsl --shutdown
  
Put the following settings into `C:\Users\<your_user_name>\.wslconfig`. Remember DON'T ADD THE EXTENSION AT THE END. The settings in `.wslconfig` are as follows:
 
    [wsl2]
    memory=32GB # Limits Ubuntu memory
    diskSizeLimit=200GB # Limits how much Ubuntu can grow
  
Save and quit, restart WSL-2, you can use htop command to check, it should reflect the whole memory for you.

## Compact the VHDX file

The VHDX file is the file in Windows that contains Ubuntu. After cleaning files in Ubuntu, the VHDX file can have the same size. To compact it go to Command line:

```cmd
diskpart
select vdisk file="C:\Users\hoaph\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\ext4.vhdx"
compact vdisk
exit
```


