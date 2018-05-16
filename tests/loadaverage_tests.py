import unittest 

from sensesagent.collectors.loadaverage import LoadAverageCollector

from sensesagent import log

class TestLoadAverageCollector(unittest.TestCase):
    
    def setUp(self):
        
        lac = LoadAverageCollector(template="configs/loadaverage.json")
    
    
    def test_can_load_template(self):
        
        pass


if __name__ == "__main__":
    
    unittest.main()
    
    
    