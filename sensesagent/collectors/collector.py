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

from sensesagent import log

if platform.architecture()[0] == '64bit':
    MAX_COUNTER = (2 ** 64) - 1
else:
    MAX_COUNTER = (2 ** 32) - 1


class Collector(object):
    
    def __init__(self, template=None, ):
        
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Instantiating Collector")
        self.metrics = {}
        self.template = template
    
    def collect_metrics(self):
        """Implements gathering metrics"""    
        raise NotImplementedError
    
    def process_template(self):
        """Updates the template json """
        pass
    
    def load_template(self):
        
        pass
    
    