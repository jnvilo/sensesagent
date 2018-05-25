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
import psutil
from multiprocessing import cpu_count
from sensesagent.collectors.collector import Collector


class LoadAverageCollector(Collector):
    """
    Collects Load average. This collector exposes the following metrics:
        load_1_minute - The 1 minute load average
        load_5_minute - The 5 minute load average
        load_15_minute - The 15 minute load average
    """       

    def collect_metrics(self):
        """Implements gathering the metrics and filling up our 
        metrics object
        
        """
            
        load_1_minute, load_5_minute, load_15_minute = os.getloadavg()
        cpu_percent = psutil.cpu_percent()
    
        self.add_metric("load_1_minute", load_1_minute) 
        self.add_metric("load_5_minute", load_5_minute)
        self.add_metric("load_15_minute", load_15_minute) 
        
if __name__ == "__main__":
    
    lac = LoadAverageCollector()
    
    for key in lac.metrics.keys():
        print(key)
    
    
   
    
    

