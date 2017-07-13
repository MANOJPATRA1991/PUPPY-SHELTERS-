# PUPPY-SHELTERS

## Introduction
This is an optional project completed as part of Part 3 *The Backend: Databases & Applications* of [Udacity Full Stack Nanodegree course](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004/).

## Table of Contents
1. [Installation](#installation)
2. [Description](#description)
3. [Reference](#reference)
4. [License](#license)

### Installation

**NOTE**: 

This project was built on **Windows 10** OS. All the interaction with the Virtual Machine was done through **Command Prompt on Windows**.

(**Do not use Git Bash for this project. It simply won't work**.)

1. Python

The source code for this project is written in [Python v3.6.1](https://www.python.org/downloads/) programming language.
For direct download of version 3.6.1 [click here](https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe).

2. Code Validators

The source code was checked against bugs and quality using **Pylint** tool, **PEP8** tool and [PEP8 online check](http://pep8online.com).

To install Pylint:

```
pip3 install pylint
```

To check Python file using Pylint:

```
pylint fileName.py
```

To install pep8:

```
pip3 install pep8
```


To check Python file using pep8:

```
pep8 fileName.py
```

3. Virtual Box

To run the Virtual Machine, first, we need to download it and then install it.
Virtual Box can be downloaded from [here](https://www.virtualbox.org/wiki/Downloads).

4. Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. 
Vagrant can be downloaded from [here](https://www.vagrantup.com/downloads.html).

5. `psycopg2` python module is required. To install:

```
pip3 install psycopg2
```

6. SQLAlchemy

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. For instructions on download and installation [click here](https://www.sqlalchemy.org/download.html).

### Description

Design a database server to keep track of puppies used by the sheltes for adoption.

##### Exercise Requirements

Using SQLAlchemy perform the following queries on your database:
1. Query all of the puppies and return the results in ascending alphabetical order
2. Query all of the puppies that are less than 6 months old organized by the youngest first
3. Query all puppies by ascending weight
4. Query all puppies grouped by the shelter in which they are staying

##### Executing the program

1. Create a new folder.

2. If the folder doesn't already contain a Vagrantfile. Run the following command to create one.
        
```
vagrant init
```
    
3. To start the virtual machine, from your local directory, run the following command:
        
```
vagrant up
```

4. Then to drop a full-fledged SSH session, run the following command:
        
```
vagrant ssh
```

5. Download and run **database_setup.py** file to create the database. 

6. Download and run **puppypopulator.py** file to populate your database with puppies and shelters.

7. Download and run the **puppy_query.py** file to do queries.


### Reference
1. [Python Documentation](https://docs.python.org/3/)
2. [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
3. [PEP8](https://www.python.org/dev/peps/pep-0008/)
4. [Vagrant](https://www.vagrantup.com/)
5. [Oracle VM Virtual Box](https://www.virtualbox.org/)
6. [PostgreSQL](https://www.postgresql.org/)
7. [SQLAlchemy](https://www.sqlalchemy.org/)

### License
The content of this repository is licensed under [MIT](https://choosealicense.com/licenses/mit/).
