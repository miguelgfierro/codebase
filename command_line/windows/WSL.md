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

## Configure WSL to allocate the maximum memory

First, close all open WSL-2 and open CMD, enter the following command:

    wsl --shutdown
  
Put the following settings into `C:\Users\<your_user_name>\.wslconfig`. Remember DON'T ADD THE EXTENSION AT THE END. The settings in `.wslconfig` are as follows:
 
    [wsl2]
    memory=32GB # Limits VM memory
  
Save and quit, restart WSL-2, you can use htop command to check, it should reflect the whole memory for you.
