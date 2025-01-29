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

## 3. Do the projects

Once you are ready, you can start on the programming projects.
You will be continuing to practice your Git/GitHub and programming skills as you go
along.
You will be continuing to develop these skills as long as you keep programming,
so take time to review as needed.

Set-up instructions:
1. [Create a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) of this repository.
2. Create a branch for the first exercise (see below).
3. When you are ready for feedback,
[create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request#creating-the-pull-request)
to this repository from the branch on your fork. I will give you feedback directly on your pull request.
4. Continue on in this way, creating a new branch for each exercise or part of a project.

Please keep the `main` branch of your fork clean and do all of your work on
separate branches.
This way, if you notice a typo, you can do so on your main branch and create a
pull request that I can merge to fix it.
Eventually, you may also wish to contribute to the instructions, or contribute
projects of your own!

Once you are ready with your fork and branch, you can work through the projects in the following order:

1. [Introduction, Part 1: Cheminformatics](projects/00_cheminformatics/background.ipynb) (includes an exercise)
2. [Introduction, Part 2: Quantum Chemistry](projects/01_quantum-chemistry/background.ipynb)
3. [Project 1, Part 1: Hessian Calculation](projects/02_hessian/background.ipynb)
3. [Project 1, Part 2: Vibrational Analysis](projects/03_vibrations/background.ipynb) (coming soon)

[^1]:  https://learn.microsoft.com/en-us/windows/wsl/install#install-wsl-command)
