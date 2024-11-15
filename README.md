# Programming Projects

## 1. Set up a Linux terminal

If you are on a Mac or Linux machine, you already have a Linux terminal and no further set-up is required.

If you are on a Windows machine, follow these instructions to install the Windows Subsystem for Linux (WSL): [^1]
1. Open PowerShell in administrator mode by right-clicking and selecting "Run as administrator".
2. Enter the following command into the command prompt:
   ```
   wsl --install
   ```
3. Re-start your machine.

This creates a miniature Linux operating system (OS) on your computer, which you can access through a terminal. You can can open this Linux terminal by searching "WSL" in your taskbar clicking "Open". You can also click "Pin to taskbar" for easier access.

**Note**: This WSL terminal is *not* running on the Windows OS. It is running on an Ubuntu Linux OS. You will need to keep this in mind if you encounter any OS-specific instructions.

## 2. Learn the basics

To learn the basics of navigating the command line, working with `git`, and programming in Python, complete the following [lessons from Software Carpentry](https://software-carpentry.org/lessons/):
1. [The Unix Shell](https://swcarpentry.github.io/shell-novice)
2. [Version Control with Git](https://swcarpentry.github.io/git-novice/)
3. [Programming with Python](https://swcarpentry.github.io/python-novice-inflammation/)
4. [Plotting and Programming in Python](https://swcarpentry.github.io/python-novice-gapminder)

**Reminder**: If you are running in WSL and encounter any OS-specific instructions, follow the instructions for the **Linux OS** (specifically Ubuntu, which is a flavor of Linux).

Optionally, if you plan to work with databases, you may also wish to complete the lesson [Using Databases and SQL](https://swcarpentry.github.io/sql-novice-survey).

[^1]:  https://learn.microsoft.com/en-us/windows/wsl/install#install-wsl-command)
