# sensesagent
A monitoring agent to gather system metrics and send to data to backend

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  

- [Development Setup:](#development-setup)
  - [WSL and Ubuntu setup](#wsl-and-ubuntu-setup)
  - [Fedora](#fedora)
- [Modifying the Code and layout of code.](#modifying-the-code-and-layout-of-code)
- [Code Layout And Modules](#code-layout-and-modules)
  - [Non Git directories](#non-git-directories)
  - [The senseagent Modules](#the-senseagent-modules)
    - [senseagent.master](#senseagentmaster)
    - [senseagent.collectors](#senseagentcollectors)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## Development Setup: 

The current code is developed in WSL and also tested on Fedora 26. The sources include a makefile that will build a p
ython binary within the development directory and as a result any system that can build the latest python3 release ca
n also be used for development. The following instructions show how to do this. 

***Why do we build a version of python3 within the development code? - This is so that we can ensure that the development environment is the same on all platform and also allows us to have multiple versions of python as can be show below where we can execute __**make**__ and tell it to use a different version other than the default***


### WSL and Ubuntu setup

The default distro for WSL is ubuntu and hence the following setup also applies if developing for ubuntu. 

``` 
  sudo apt install libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev 
  sudo apt install libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev  gcc
``` 
And now we actuall execute make to prepare our development environment.  The first time we do this will take some time because it will download and built the latest python binary.
``` 
  make 
```

The above will install the required libraries and build the latest python into sensesboard/buid/python3.x. and symlink it to senseboard/virtualenv. It will also download and install all the required python libraries. 

### Fedora 
Using Fedora is same as in WSL or Ubuntu above except that we install the required libs differently. 

```
  # yum -y groupinstall development
  # yum -y install zlib-devel
```


After running the above commands as root, or via sudo, we can now do 

```  
make
```

## Modifying the Code and layout of code.

After the initial setup of the development system, we can now start hacking away at the code. Note that you  can also develop/test with a specific version of Python:

    make PYTHON_VERSION=2.7.11 test # Will set virtualenv also to point to this version of python. 


## Code Layout And Modules

After running make for the first time , you should have the current top directory  tree: 

```
  ├── build
  ├── configuration.mk
  ├── docs
  ├── LICENSE
  ├── Makefile
  ├── make-includes
  ├── README.md
  ├── requirements.txt
  ├── sensesagent
  ├── sensesagent.egg-info
  ├── setup.cfg
  ├── setup.py
  ├── test
  ├── tests
  └── virtualenv -> build/python/virtualenv-3.6.0
```

### Non Git directories

Not directory build, symlink virtualenv,  and senseagent.egg-info are temporary file and are not committed into git. They are ignored using the .gitignore.
The actual module code lives in senseagent. 

### The senseagent Modules
  
  The senseagent module is made up of:
    
    senseagent.master
    senseagent.collectors
    
 
#### senseagent.master
  TODO: Document this module
  
#### senseagent.collectors
The actual work of collecting metrics is implemented in the imaginatively named collectors modules. 
  TODO: Document each collector


  

  
