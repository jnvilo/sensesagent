# coding=utf-8
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from future.utils import raise_
from future.utils import raise_with_traceback
from future.utils import raise_from
from future.utils import iteritems

import os
import logging

from jinja2 import Template

from multiprocessing import cpu_count
from sensesagent import log

from sensesagent.collectors.collector import Collector
from sensesagent.utils import DictionaryUtility

class LoadAverageCollector(Collector):
    """
    Collects Load average 
    """
    
    def __init__(self, template_path=None): 
        
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug("Instantiating LoadAverageCollector(template_path=\"{}\")".format(template_path))
        super().__init__(template_path=template_path)
    
    
    def collect_metrics(self):
        """Implements gathering the metrics and filling up our 
        metrics object"""
        
        
        load_1_minute, load_5_minute, load_15_minute = os.getloadavg()
        num_cpu = cpu_count()
    
        return  DictionaryUtility.to_object({ "load_1_minute": load_1_minute, 
                 "load_5_minute": load_5_minute, 
                 "load_15_minute": load_15_minute, 
                 "num_cpu": num_cpu})
        
    def process_template(self):
        
        metric = self.collect_metrics()
        #self.template = """{ "1minute" : {{metric.load_1_minute}} }"""
        json_str = Template(self.template).render(metric=metric)
       
        return json_str
    
    def format_metric(self):
        """Formats the metric with the given template."""
        pass
        
    
    

