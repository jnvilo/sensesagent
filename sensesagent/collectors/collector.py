# coding=utf-8
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from future.utils import raise_
from future.utils import raise_with_traceback
from future.utils import raise_from
from future.utils import iteritems

import platform
import logging 
from pathlib import Path 

from sensesagent import log

if platform.architecture()[0] == '64bit':
    MAX_COUNTER = (2 ** 64) - 1
else:
    MAX_COUNTER = (2 ** 32) - 1

class TemplateLoader(object): 
    """Loads template"""
    
    def __init__(self):
        pass
    

class Collector(object):
    
    def __init__(self, template_path=None, metric=None):
        
        self.logger = logging.getLogger(self.__class__.__name__)
        #self.logger.debug("Instantiating Collector")
        self.metric = {}
        self.template_path = template_path
        self.template = self.load_template()
    
    
    
    def collect_metrics(self):
        """Implements gathering metrics"""    
        raise NotImplementedError
    
    def process_template(self):
        """Updates the template json """
        
        raise NotImplementedError
    
    def load_template(self):
        """
        Loads a template used to create the json data to be sent to the 
        server. 
        
        if template_path is not provided then it will look for a template 
        using formated as  <self.__class__.__name__>.template in the 
        following directory sequence: 
        
        .conf/<self.__class__.__name__>.template
        /etc/sensesagent/conf/<self.__class__.__name__>.template
        
        """
        if self.template_path == None: 
            local_path = "conf/collector_templates/{}.template".format(self.__class__.__name__)
            conf_files = [local_path,
                          "/etc/sensesagent/conf/collector_templates/{}".format(local_path)
                        ] 
            
            for conf_file in conf_files:    
                try:
                    with open(conf_file, "r") as f:
                        template = f.read()
                        return template
                except TypeError: 
                    if self.template_path == None: 
                        #If we get here then we did not manage to find a template file
                        msg = "Failed to Load Template File for {}".format(self.__class__.__name__)
                        self.logger.fatal(msg)
        else: 
            #Just load what we were given then:
            with open(self.template_path, "r") as f:
                template = f.read()
                return template            
            
def gather_metric(self, name, value):
    
        pass
    
if __name__ == "__main__":
    
    c = Collector()