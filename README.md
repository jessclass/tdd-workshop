# tdd-workshop
Test-Driven Development (TDD) Workshop materials

Welcome to the Test-Driven Development (TDD) Workshop! We will spend a couple 
hours together learning about TDD and applying it to simple Python programs.

This course assumes basic knowledge of programming in Python, but not much else!

# Environment Setup
## System Requirements
Some prerequisites for your system:
*   Linux (samples in course use Ubuntu)
    *   If you're using Windows 10, you can run Linux natively using WSL! 
        Installation instructions [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
*   Python 3 (samples in course use Python 3.6)
*   IDE of your choosing (e.g., VS Code, Sublime, Atom)

## Pre-Workshop Setup
-   Download this repository to your local system. Here are a couple ways you 
    can do that:

    Using git:

        git clone https://github.com/supernaut11/tdd-workshop.git

    Using curl:

        curl -LO https://github.com/supernaut11/tdd-workshop/archive/master.zip
        unzip master.zip

    Using a web browser:

        https://github.com/supernaut11/tdd-workshop/archive/master.zip

-   Install the python3-venv package

        sudo apt install python3-venv

-   Run the initialization script

        ./init.sh

    Note that 'python3' must be defined for the script to work. If it isn't, 
    create an alias or symbolic link to your Python 3 installation and name 
    it 'python3'.

