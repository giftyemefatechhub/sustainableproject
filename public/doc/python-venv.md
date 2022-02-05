Work in a Python virtual environment
===========================

A virtual environment in Python means you can install the tools and libraries needed within the projects files.

The benefit is that you do not need to install these globally in your operatingsystem, you can isntall them specifically for each project.

These are the basic approch when creating and working with a virtual environment.



Create and use a virtual environment
---------------------------

Create the basis for the virtual environment.

```
python3 -m venv .venv
ls -l .venv
```

Activate the particular environment (you can have several environments in its own directory).

```
. .venv/bin/activate
```

Install packages from `requirements.txt`, or from pip directly.

```
python3 -m pip install -r requirements.txt
python3 -m pip list
```

It is preferrable to use a `requirements.txt` for the needed packages and tools. This file is a text files with the packages to install and one can set explicitly the version to be installed.

Deactivate the virtual environment and stop using it.

```
deactivate
```

Then activate it again when you want to use it once more.



References
--------------------------

* [12. Virtual Environments and Packages](https://docs.python.org/3/tutorial/venv.html)
* [venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
