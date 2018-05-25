# coding=utf-8
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

from future.utils import raise_
from future.utils import raise_with_traceback
from future.utils import raise_from
from future.utils import iteritems


#Std Lib imports
import platform
import logging 
from pathlib import Path 

#third party libs imports
from jinja2 import Template
from datetime import datetime

#sensesagent imports
from sensesagent import log
from sensesagent.utils import DictionaryUtility
from sensesagent import exceptions



if platform.architecture()[0] == '64bit':
    MAX_COUNTER = (2 ** 64) - 1
else:
    MAX_COUNTER = (2 ** 32) - 1


class Collector(object):
    """
    The base class for all collectors. 
    """
    
    def __init__(self, template_path=None, metric=None, config=None):
        
        cls_name = self.__class__.__name__
        
        #if metric is None:
        #    metric= {}
        self.logger = logging.getLogger(cls_name)
        self.logger.debug("Instantiating {}".format(cls_name))
        self.metric_dict = {}
        self.template_path = template_path
        self.template = self.load_template()
        self.config = config
    
        #Convert the config into a dictionary 
        self.metric_dict.update( {"config": config} ) 
    
    @property
    def json(self):
        return self.process_template()
    
    @property 
    def metrics(self):
        """
        Returns the metrics_dict. using this instead of directly 
        accessing metrics_dict ensures that we have executed collect_metrics
        first. 
        """
        # this is just a facade for collect_metrics. Will 
        # rewrite this to use a MetricObject and migrate 
        # processing to it. 
        #return DictionaryUtility().to_object(self.metric_dict)
        #the metric 
        
        if len(self.metric_dict) == 1: 
            #Two things is possilbe. Either the implementation has no metrics
            # or most probably we have not yet called collect_metrics
            
            self.collect_metrics()
            
        return self.metric_dict
    
        
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
            
            #local_path is relative to the entry point file. In this case the 
            #agent is started in senses.py at the topmost directory of the source
            #code. 
            local_path = "conf/collector_templates/{}.template".format(self.__class__.__name__)
            
            #relative_path is a path that leads to senses.py which is 2 directories
            #above  this file. 
            senses_path = Path(__file__).parent.parent.parent
            relative_path = Path(senses_path, local_path)
            
            #TODO: Test using /etc as the path.
            conf_files = [local_path, relative_path.as_posix(), 
                          "/etc/sensesagent/conf/collector_templates/{}".format(local_path)
                        ] 
            
            for conf_file in conf_files:    
                try:
                    with open(conf_file, "r") as f:
                        template = f.read()
                        return template
                except FileNotFoundError as e: 
                    # Ignore the FileNotFoundError because we shall keep going 
                    # through the rest of the conf_files search. 
                    pass
            #If we arrive to here then it means template not found.

            cls_name = self.__class__.__name__
            message = "Could not load template for {}".format(cls_name)
            raise exceptions.TemplateFileNotFound(message)
        else: 
            #Just load what we were given then:
            #TODO: This will bomb out if the provided template is not working. 
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
          

          
    def __str__(self): 
      
        result = ""
        for metric in self.metrics: 
            result = result + "{}:{}\n".format(metric, self.metrics[metric])
        return result
        
        
def gather_metric(self, name, value):
    
        pass
    
if __name__ == "__main__":
    
    c = Collector()