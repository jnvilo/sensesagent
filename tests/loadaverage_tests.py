import unittest 

import os
import simplejson as json
from pathlib import Path

from sensesagent.collectors.loadaverage import LoadAverageCollector
from sensesagent import log

class TestLoadAverageCollector(unittest.TestCase):
    
    def setUp(self):
        
        #The config path is one directory above us. 
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        parent_path = Path(dir_path).parent
        template_path = Path(parent_path, "conf/collector_templates/LoadAverageCollector.template")
        self.lac = LoadAverageCollector(template_path=template_path.as_posix())
    
    def test_can_process_template(self):
        
        json_str = self.lac.process_template()
        print(json_str)
        
        
    def test_metric(self):
        pass
        
    def test_json(self):
        x = json.loads(self.lac.json)
        print(x)
        
if __name__ == "__main__":
    
    unittest.main()
    
    
    