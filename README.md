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

With some working knowledge of Unix, Git, and Python, you are ready to start the programming projects!
You will be continuing to practice these skills as you go along and, in fact, will be doing so as long as you continue programming, so take time to review as needed.

### Set-up

Before starting the projects, follow these instructions to set up your repository and your environment:
1. [Create a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) of this repository.
2. [Clone the fork](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) to your machine.
3. [Install Pixi](https://pixi.sh/latest/#installation) and run `pixi install` inside the repository. [Pixi](https://pixi.sh/latest/basic_usage/) is the package manager that will create your environment.[^2]
5. [Create a new branch](https://stackoverflow.com/a/6824219) for the first tutorial.
6. Complete the tutorial, saving your work to this branch.
7. [Create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request#creating-the-pull-request) from your branch to this repository
to submit your work for feedback when ready. I will give feedback directly on your pull request.

Repeat steps 5-7 as you go through the tutorials, creating a new branch for each one.
In doing so, you may wish to branch off of your previous working branch, rather than the `main` branch,
so that you have your previous code to start from.

**Note**: Please keep the `main` branch of your fork clean and do all of your work on
separate branches.
This way, if you notice a typo, you can easily fix it on main branch and create a
pull request for me to merge.


### VS Code

I highly recommend doing your work for these projects in [VS Code](https://code.visualstudio.com/docs).
This is a huge help in navigating your code.
For example, to see the code for a function you are calling, you can right click and select "Go to Definition".

If you, like me, like to use [Vim](https://youtu.be/9n1dtmzqnCU?si=QHMSaJrciy0tuJUZ) for text-editing, I recommend the [VS Code Vim plugin](https://code.visualstudio.com/docs/getstarted/getting-started).


### Projects

Once you are ready with your fork and branch, you can work through the projects in the following order:

1. [Introduction, Part 1: Cheminformatics](projects/00_cheminformatics/background.ipynb) (includes an exercise)
2. [Introduction, Part 2: Quantum Chemistry](projects/01_quantum-chemistry/background.ipynb)
3. [Project 1, Part 1: Hessian Calculation](projects/02_hessian/background.ipynb)
3. [Project 1, Part 2: Vibrational Analysis](projects/03_vibrations/background.ipynb) (coming soon)

Happy programming!

[^1]: https://learn.microsoft.com/en-us/windows/wsl/install#install-wsl-command)
[^2]: You can activate the Pixi environment using the command `pixi shell`.
