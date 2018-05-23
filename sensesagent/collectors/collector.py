# coding=utf-8
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from future.utils import raise_
from future.utils import raise_with_traceback
from future.utils import raise_from
from future.utils import iteritems


from jinja2 import Template


import platform
import logging 
from pathlib import Path 

from sensesagent import log
from sensesagent.utils import DictionaryUtility



if platform.architecture()[0] == '64bit':
    MAX_COUNTER = (2 ** 64) - 1
else:
    MAX_COUNTER = (2 ** 32) - 1

class TemplateLoader(object): 
    """Loads template"""
    
    def __init__(self):
        pass
    

class Collector(object):
    
    def __init__(self, template_path=None, metric=None, config=None):
        
        cls_name = self.__class__.__name__
        
        if metric is None:
            metric= {}
        self.logger = logging.getLogger(cls_name)
        self.logger.debug("Instantiating {}".format(cls_name))
        self.metric_dict = metric
        self.template_path = template_path
        self.template = self.load_template()
        self.config = config
    
        #Convert the config into a dictionary 
        
        self.metric_dict.update( {"config": config} ) 
        
        
    
    @property
    def json(self):
        return self.process_template()
    
    @property 
    def metric(self):
        """
        Returns a metric object
        """
        # this is just a facade for collect_metrics. Will 
        # rewrite this to use a MetricObject and migrate 
        # processing to it. 
        #return DictionaryUtility().to_object(self.metric_dict)
        #the metric 
        
        
    def collect_metrics(self):
        """Implements gathering metrics"""    
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
    
    def process_template(self):
        """
        Applies the metric dictionary to the template and returns it as 
        a json str.
        """
        # Call collect_metrics to ensure we update the metric_dict which 
        # contains all the available metrics that the template will use. 
        self.collect_metrics()
        
        #The jinja2 template
        
        json_str = Template(self.template).render(metric=self.metric_dict)
       
        return json_str
     
    
    def add_metric(self, name, value):
        self.metric_dict.update({ name:value})
          
          
          
def gather_metric(self, name, value):
    
        pass
    
if __name__ == "__main__":
    
    c = Collector()