from __future__ import print_function
import unittest
import mock
import os.path
from pathlib import Path 

from tests.utilities import module_function_name

from sensesagent.main import SensesAgentConfig
from sensesagent.main import SensesAgent

class TestSensesAgentConfig(unittest.TestCase):
    
    #@mock.patch(module_function_name(print))
    #def test_should_print_hello_world(self, mock_print):
       
       #pass

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
           
        
class TestSensesAgent(unittest.TestCase):
    
    def test_can_get_collector_class_from_built_in(self):
        
        start_dir = Path(os.path.dirname(os.path.realpath(__file__)))
        sa = SensesAgent(start_dir)   
    
        sa.get_collector_class("loadaverage.LoadAverageCollector")
        