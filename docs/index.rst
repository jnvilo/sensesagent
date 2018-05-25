.. SensesAgent documentation master file, created by
   sphinx-quickstart on Wed May 16 08:26:00 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SensesAgent
==========================

.. sidebar:: SensesAgent Cloud

    Although sensesagent is a full fledge metric collection software and framework, it was written with the main 
    purpose of testing and development of SensesCloud. As a result SensesAgent is also a framework for mocking or 
    simulating IOT data. By simply modifying the configurations, it can be used to send data to your IOT backend. 
    
    Currently it only supports http/https method of sending data but MQTT is high on the roadmap. 

SensesAgent is a systems metric collection framework and runtime. It can be used as provided to gather system metrics and send gathered metrics to an online service. 
It is also a framework that can be used to simulate or mock metrics to send to remote systems. 

SensesAgent is developed for SensesCloud. However it can be easily configured via the sensesagent.conf file to upload metrics to a different service. The format of the data sent can also be easily modified through the data template files.



Creating new collectors that gathers metrics is currently supported in python. A basic 
collector for example that collects loadaverage is as shown below: 



    
    This is a test

.. toctree::
   :maxdepth: 2
   
   users-guide.rst
   dev-guide.rst
