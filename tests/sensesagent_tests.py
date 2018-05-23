from __future__ import print_function
import unittest
import mock
import os.path
from pathlib import Path 

import logging
from tests.utilities import module_function_name

from sensesagent  import SensesAgentConfig
from sensesagent  import SensesAgent

class TestSensesAgentConfig(unittest.TestCase):
    
    #@mock.patch(module_function_name(print))
    #def test_should_print_hello_world(self, mock_print):
    
    def setUp(self):
        self.logger = logging.getLogger(self.__class__.__name__)
      
    def test_can_load_config(self):
        
        pass
    
    
    def test_can_find_config_path_in_the_local_dir(self):
        """
        We test 
        
        """
        start_dir = Path(os.path.dirname(os.path.realpath(__file__)))
        
        sa = SensesAgentConfig(start_dir)
        sa.find_config_path()
        
        self.assertTrue(1)
        
    def test_can_load_config_file(self):
        """
        Ensures that we can open the sensesagent.conf file. 
        """
        start_dir = Path(os.path.dirname(os.path.realpath(__file__)))
        
        sa = SensesAgentConfig(start_dir)
        sa.config 
           
    def test_get_collectors(self):
        
        curr_path = Path(os.path.dirname(os.path.realpath(__file__)))
        start_dir  = curr_path.parent.as_posix()
        
        saconfig = SensesAgentConfig(start_dir)
        print(saconfig.config_path)
        print(saconfig.start_dir)
        
        self.logger.info("Loading Collectors config")

        for collector in saconfig.config.get("Collectors"):
            self.logger.info("Loaded collector: {}".format(collector))
        
        
class TestSensesAgent(unittest.TestCase):
    
    def test_can_get_collector_class_from_built_in(self):
        
        start_dir = Path(os.path.dirname(os.path.realpath(__file__)))
        sa = SensesAgent(start_dir)   
    
        sa.get_collector_class("loadaverage.LoadAverageCollector")
        
    def test_run_collectors(self):
        
        start_dir = Path(os.path.dirname(os.path.realpath(__file__)))
        sa = SensesAgent(start_dir)       
        sa.run_collectors()
    

    



