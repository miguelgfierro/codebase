#!/bin/bash
#
# 1) Install Remote VSCode (https://github.com/rafaelmaiolla/remote-vscode). Go to the Extensions 
# page and search for Remote VSCode.
#
# 2) In your Linux Virtual Machine, execute the following command in your terminal to install rmate:
# $ sudo wget -O /usr/local/bin/rmate https://raw.github.com/aurora/rmate/master/rmate
# $ sudo chmod a+x /usr/local/bin/rmate
#
# 3) Go back to your Visual Studio Code and open up the command palette (CTRL+P for Windows and 
# CMD+P for Mac) then execute the >Remote: Start Server command.
#
# 4) Once the server is ready, open up a new terminal and connect to your Linux VM using the following command:
# $ ssh -R 52698:localhost:52698 VIRTUAL_MACHINE_IP_ADDRESS
#
# 5) In your terminal, execute rmate with the file that you want to open locally in your VSCode.
# $ rmate demo.py
#
# source: https://medium.com/@prtdomingo/editing-files-in-your-linux-virtual-machine-made-a-lot-easier-with-remote-vscode-6bb98d0639a4
#

ssh -R 52698:localhost:52698 VM_IP_OR_DNS_ADDRESS

