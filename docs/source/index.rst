.. SensesAgent documentation master file, created by
   sphinx-quickstart on Wed May 16 08:26:00 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SensesAgent
==========================

SensesAgent is a systems metric collection framework and runtime. It can be used as provided to gather system metrics and send gathered metrics to an online service.

SensesAgent is developed for SensesCloud. However it can be easily configured via the sensesagent.conf file to upload metrics to a different service. The format of the data sent can also be easily modified through the data template files.


.. code-block:: python

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
       

   

.. topic: Test
    
    This is a test

.. toctree::
   :maxdepth: 2
   
   users-guide.rst
   dev-guide.rst
