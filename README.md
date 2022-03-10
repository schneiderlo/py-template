# Python Template Project

A simple python template for getting up and running quickly.

# Getting Started

## Use the Github template

First, click the "Use this template" green button located at the top of this page. Follow the instruction to create a new repository in your Github account. It will have the same contents of this project.

## Build Instructions

### Dependencies

This project relies on [doit](https://pydoit.org/) and [pydoit-project-builder](https://github.com/schneiderlo/pydoit-project-builder) which can be installed with:

```pip install doit pydoit-project-builder```

### Setup the project

The first step consist in creating a virtual environment which will contains the project dependencies. Run the following command:

```doit setup```

It will create a virtual environment and install the dependencies find inside the setup.py.

### Test the project

To test the project run the following command:

```doit test```

### Other commands

Type `doit list` to see all available commands.
