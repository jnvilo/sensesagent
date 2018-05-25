SensesAgent Users Guide!
***************************************


Installation
==============

Install via github:
--------------------

::

    git clone https://github.com/jnvilo/sensesagent.git
    
    
Install via pip
-----------------
    pip install sensesagent
    
.. note::
    Current version 0.1 does not contain any launcher. So although technically 
    we can install senseagent via pip. It is not possible to run it. Please
    use git instead. 
    
    Install via pip only if using sensesagent as a library/framework.



Configuration
====================

Configuration is done through conf/sensesagent.conf. 

.. note::

    It is assumed that you are running on a system that has python3.5 or greater already installed.
    
    
Configuration files can be found in the conf directory. The directory tree of the conf directory is as follows::

    ├── collector_templates
    │   ├── collector.template
    │   ├── CpuTimesCollector.template
    │   ├── LoadAverageCollector.template
    │   └── SystemStatsCollector.template
    └── sensesagent.conf

An example configuration file for SensesCloud is as follows:


.. code-block:: python.
    :linenos:
    
    ################################################################################
    # Main section contains agent configuration
    ################################################################################
    [Main]
    url = https://sensescloud.herokuapp.com/APIv1/deviceData
    
    #The default interval that a collector gathers data and send. 
    interval=5  

    
    ################################################################################
    #Collector configurations
    ################################################################################
    
    
    [Collectors]
        #by default we look for the collector class implemantation 
        #sensesagent.collectors [Implemented as /sensesagent/collectors/]
        
        [[SystemCollector1]]
            class=LoadAverageCollector.LoadAverageCollector
            name=SystemCollector
            update=5
            device_secure_id = "WMyQTsETnC"
            device_key = "MoBo5eQqRZ"
            device_name = "Desktop"  
    
        
        [[SystemCollector2]]
            name="My Testing of CPUTimes Collector"
            class= CpuTimesCollector.CpuTimesCollector
            update=5
            device_name = "DeviceSim.CPUTimes"
            device_key = "TJfAtY5omq"
            device_secure_id = "SOmLidnCBO"
        


The above config file is a basic configuration that defines:

#. The url where to POST the metric data as defined by the template for the collectors.
#. A collector implemented by *
