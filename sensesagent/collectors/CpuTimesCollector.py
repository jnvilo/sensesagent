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


class CpuTimesCollector(Collector):
    """
    Collects system statistics. This Collector exposes the following metrics
    """       

    def collect_metrics(self):
        """Implements gathering the metrics and filling up our 
        metrics object"""
            
        load_1_minute, load_5_minute, load_15_minute = os.getloadavg()
        num_cpu = cpu_count()
    
       
        self.add_metric("cpu_percent", psutil.cpu_percent())
        data = psutil.cpu_times_percent()
        #scputimes(user=7.4, nice=0.0, system=4.9, idle=87.5, iowait=0.0, irq=0.2, softirq=0.0, steal=0.0, guest=0.0, guest_nice=0.0)    
        self.add_metric("user", data.user)
        self.add_metric("nice", data.nice)
        self.add_metric("idle", data.idle)
        self.add_metric("iowait", data.iowait)
        self.add_metric("irq", data.irq)
        self.add_metric("soft_irq", data.softirq)
        self.add_metric("guest", data.guest)
        
if __name__ == "__main__":
    
    ssc = CpuTimesCollector()
    
    print(ssc)
    print(ssc.metrics)
        
    try:
        ssc.metrics.pop("config")
    except KeyError as e:
        pass    
    
    for key in ssc.metrics:
       
        
        #print(key, ssc.metrics.get(key))
    
        print("""\t "{}": {{{{metric.{}}}}},   """.format(key, key))

   
    
    

