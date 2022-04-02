# Windows Subsystem for Linux (WSL)

## Configure WSL to allocate the maximum memory

First, close all open WSL-2 and open CMD, enter the following command:

  wsl --shutdown
  
Put the following settings into C:\Users\<your_user_name>\.wslconfig. Remember DON'T ADD THE EXTENSION AT THE END. The settings in .wslconfig are as follows:
 
  [wsl2]
  memory=32GB # Limits VM memory
  
Save and quit, restart WSL-2, you can use htop command to check, it should reflect the whole memory for you.
