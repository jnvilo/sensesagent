import unittest 

from sensesagent.collectors.collector import Collector

from sensesagent import log

class CollectorTestCase(unittest.TestCase):
    
    def setUp(self):
        
        self.lac = Collector(template_path="conf/collector_templates/collector.template")
        
    
    def test_can_load_template(self):
        
        with open("conf/collector_templates/collector.template", "r") as f:
            template = f.read()
        
        
        self.lac.load_template()
        self.assertEqual(self.lac.template, template)
        
if __name__ == "__main__":
    
    unittest.main()
    
    
