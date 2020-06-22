# tdd-workshop
Test-Driven Development (TDD) Workshop materials

Welcome to the Test-Driven Development (TDD) Workshop! We will spend a couple 
hours together learning about TDD and applying it to simple Python programs.

This course assumes basic knowledge of programming in Python, but not much else!

# Environment Setup
## System Requirements
Some prerequisites for your system:
*   Linux dev environment (samples in course use Ubuntu 18.04 LTS)
    *   If you're using Windows 10, you can run Linux natively using WSL! 
        Installation instructions [here](https://docs.microsoft.com/en-us/windows/wsl/install-win10).
    *   If you want to create a VM, check out [this instructional video](https://www.youtube.com/watch?v=diIW3fgewhI)
        on creating a VirtualBox VM for Ubuntu.
*   Python 3 (samples in course use Python 3.6)
*   IDE of your choosing (e.g., VS Code, Sublime, Atom)

## Pre-Workshop Setup
1.  Download this repository to your local system. Here are a couple ways you 
    can do that:

    Using git:

        git clone https://github.com/supernaut11/tdd-workshop.git

    Using curl:

        curl -LO https://github.com/supernaut11/tdd-workshop/archive/master.zip
        unzip master.zip

    Using a web browser:

        https://github.com/supernaut11/tdd-workshop/archive/master.zip

2.  Install the python3-venv package

        sudo apt install python3-venv

3.  Run the initialization script

        ./init.sh

    Note that 'python3' must be defined for the script to work. If it isn't, 
    create an alias or symbolic link to your Python 3 installation and name 
    it 'python3'.

4.  Make sure the Python virtual environment is behaving as expected

        . env/bin/activate

    This should result in a string (env) appearing before your shell prompt.
    Make sure that the Python modules we need are installed:

        python3 -m pytest --version
    
    Should report something like:

        This is pytest version 5.4.3, imported from <some path>
        setuptools registered plugins:
          pytest-cov-2.10.0 at <some path>
