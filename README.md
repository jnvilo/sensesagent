# sensesagent
A monitoring agent to gather system metrics and send to data to backend

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


### Code Layout: 


