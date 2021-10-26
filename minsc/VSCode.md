# VSCode

## Configuration

Use the file [vscode_settings.json](vscode_settings.json) to configure VSCode.

## Remote execution

For setting up the [SSH remote execution](https://code.visualstudio.com/docs/remote/ssh):

1. Install an OpenSSH compatible SSH client if one is not already present.
1. Install the [Remote Development extension pack](https://aka.ms/vscode-remote/download/extension). Via the extension tab, you can search for `Remote - SSH`.
1. In the Remote Explorer blade, press the wheel icon named Configure, select the file you want to save the configuration (i.e. `C:\Users\USERNAME\.ssh\config`), fill up the file following this pattern:

```
Host alias
    HostName hostname
    User user
```
