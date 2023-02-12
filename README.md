<center> <h1>0x00. AirBnB clone - The console</h1> </center>
---

## Description of the Project
This is the first step towards building our first full web application: the AirBnB clone. 
In this stage we will implements a backend interface, or console, to manage program data by:
 * puting in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances
 * creating a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
 * creating all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
 * creating the first abstracted storage engine of the project: File storage.
 * creating all unittests to validate all our classes and storage engine

## Description of the command interpreter:
A command interpreter, also known as a shell, is a program that provides a user interface for access to an operating system's services. It enables users to interact with the operating system by executing commands and providing input to the system. The shell provides a command-line interface that allows users to execute operating system commands, run scripts, and perform various other tasks.

to start the console `./console.py`

Example in Interractive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
```
Example in Non-Interractive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
```

## Authors
* **Ebenezer Ogidiolu** - *Software Engineer* - [@dsoft02](https://github.com/dsoft02)

* **Eric Taruwinga** - *Software Engineer* - [@erc-net](https://github.com/erc-net)