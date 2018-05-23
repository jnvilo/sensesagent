from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from future.utils import raise_
from future.utils import raise_with_traceback
from future.utils import raise_from
from future.utils import iteritems

from builtins import FileExistsError
from pathlib import Path
import threading
from time import sleep

version = "0.0.1"

#The above future imports helps/ensures that the code is compatible
#with Python 2 and Python 3
#Read more at http://python-future.org/compatible_idioms.html

import logging
import sys
import os
import importlib
from threading import Thread

from sensesagent import log
from sensesagent.exceptions import ConfigFileNotFound

from configobj import ConfigObj


class SensesAgentConfig(object):
    """
    Contains the configuration for sensesagent. It loads the sensesagent.conf 
    configuration file and makes them available as the .config object 
    dictionary. 
    """

    def __init__(self, start_dir, config_path=None): 

        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("Instantiating instace with __init__(config_path={})".format(config_path))
        self.start_dir = start_dir 

        self._config_path = config_path
        self._config = None

    
    @property
    def config(self):
        """configobject property. This contains the dictionary from 
        sensesagent.ini file. Example function with types documented in the docstring.

        `PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:
    
        Args:
            param1 (int): The first parameter.
            param2 (str): The second parameter.
    
        Returns:
            bool: The return value. True for success, False otherwise.
    
        .. _PEP 484:
            https://www.python.org/dev/peps/pep-0484/
    
        """
    
        if self._config == None: 
            self._config = self.load_config()

        return self._config

    @config.setter
    def config(self, config):
        self._config = config

    @property
    def config_path(self): 
        """
        Args:
            path (str): The path of the file to wrap
            field_storage (FileStorage): The :class:`FileStorage` instance to wrap
            temporary (bool): Whether or not to delete the file when the File
                instance is destructed
        
        Returns:
            BufferedFileStorage: A buffered writable file descripto        
        """
        
        if self._config_path == None: 
            return self.find_config_path()
        else: 
            return self._config_path
        
    @property
    def collectors(self):
        pass

    def load_config(self):

        #with open(self.config_path, "r") as f: 
        #config_file = f.read()
        #return config_file

        config = ConfigObj(self.config_path)
        return config

    def find_config_path(self):
        """Looks for conf directories in the following sequence: 

            1. current directory : start_dir + ./conf/sensesagent.conf
            2. conf directory above the current directory ../conf/sensesagent.conf
            3. conf in /etc/sensesagent/

            if all that fails refuse to start!
        """

        search_list = ["./conf/sensesagent.conf", 
                       "../conf/sensesagent.conf", 
                       "/etc/sensesagent/sensesagent.conf"]

        for path_str in search_list:
            test_path = Path(self.start_dir, path_str)
            if test_path.is_file():
                return test_path.as_posix()
        #If we get here then we failed!
        #try or die trying
        raise ConfigFileNotFound("Config File Not Found.")


    

class SensesAgent(object):
    """
    The SensesAgent class takes care of the following responsibilities

        1. Load the configuration
        2. Instantiate and manage the lifecycle of the collectors
        3. Ensure metrics gathhered or  created by the collectors are sent to the endpoints. 
        4. Provide remote monitoring and status of the current running agent and collectors
    """

    def __init__(self, start_dir, config_path="conf"): 
 
        #start_dir= Path(curr_dir.parent, "tests").as_posix() 
        sa = SensesAgentConfig(start_dir)
        self.config = sa.config
        self.threads = []


    def get_collector_class(self,fqcn):
        """
        Load a class using its fully qualified class name
        """

        #TODO: Add more paths here to search for more collectors. 
        search_paths = ["sensesagent.collectors",]

        for path in search_paths:
            full_path  = path + "." + fqcn
            module_path = full_path[:full_path.rfind(".")]
            class_name = full_path[full_path.rfind(".")+1:]

            module = importlib.import_module(module_path)
            my_class = getattr(module, class_name)

            return my_class


    def run_collectors(self):
        """
        Iterates through the list of collectors, ensuring to load up their 
        configurations from the config file.
        """

        fqcn = "loadaverage.LoadAverageCollector"
        t = threading.Thread(target=self.collector_runner, args=(fqcn,))
        self.threads.append(t)
        t.start()
        print("thread running")
        t.join()


    def collector_runner(self, fqcn):
        """
        This code runs inside a thread started by self.run_collectors. Its job 
        is to load the collector class provided in the fqcn, and then 
        pump it for data. 
        """
        
        MyCollector = self.get_collector_class(fqcn)
        collector = MyCollector()

        while 1:
            json_str = collector.process_template()
            sleep(5)
            print(json_str)


class SensesHttpPublisher(Thread):
    """Recieves data via a queue and takes care of sending the data."""


    def __init__(self, data_queue):
        pass


    def run(self):
        """
        Posts the data via http post. 
        """
        pass






def dev(): 

    """
    This is only used as an entry point to test the system during development.
    """

    #where are we 


    curr_dir =  Path(os.path.dirname(os.path.realpath(__file__)))
    #During Development we want to use the config files that is inside ../test/

    start_dir= Path(curr_dir.parent, "tests").as_posix() 
    sa = SensesAgentConfig(start_dir)
    #config_path = sa.find_config_path(
    print(sa.config)
    print(sa.config["Collectors"])

if __name__ == "__main__":

    dev()