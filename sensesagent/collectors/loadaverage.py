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

from multiprocessing import cpu_count
from sensesagent.collectors.collector import Collector


class LoadAverageCollector(Collector):
    """
    Collects Load average 
    """       

    def collect_metrics(self):
        """Implements gathering the metrics and filling up our 
        metrics object"""
            
        load_1_minute, load_5_minute, load_15_minute = os.getloadavg()
        num_cpu = cpu_count()
    
        self.add_metric("load_1_minute", load_1_minute) 
        self.add_metric("load_5_minute", load_5_minute)
        self.add_metric("load_15_minute", load_15_minute) 
        self.add_metric("num_cpu", num_cpu )
    
        
   
   
    
    

