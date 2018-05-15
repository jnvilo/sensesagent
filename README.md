# sensesagent
A monitoring agent to gather system metrics and send to data to backend

## Development Setup: 

The current code is developed in WSL and also tested on Fedora 26. The sources include a makefile that will build a p
ython binary within the development directory and as a result any system that can build the latest python3 release ca
n also be used for development.


### WSL and Ubuntu setup

The default distro for WSL is ubuntu and hence the following setup also applies if developing for ubuntu. 

``` 
  sudo apt install libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev 
  sudo apt install libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev   
  make 
```

The above will install the required libraries and build the latest python into sensesboard/buid/python3.x. and symlink it to senseboard/virtualenv.

You can also develop/test with a specific version of Python:

    make PYTHON_VERSION=2.7.11 test # Will set virtualenv also to point to this version of python. 

