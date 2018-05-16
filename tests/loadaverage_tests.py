import unittest 

from sensesagent.collectors.loadaverage import LoadAverageCollector

from sensesagent import log

class TestLoadAverageCollector(unittest.TestCase):
    
    def setUp(self):
        
        self.lac = LoadAverageCollector(template_path="configs/loadaverage.template")
    
    def test_can_process_template(self):
        
        json_str = self.lac.process_template()
        print(json_str)

if __name__ == "__main__":
    
    unittest.main()
    
    
    