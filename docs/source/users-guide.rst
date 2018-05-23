SensesAgent Users Guide!
***************************************

SensesAgent is a systems metric collection framework and runtime. It can be used
as provided to gather system metrics and send gathered metrics to an online service. 

SensesAgent is developed for SensesCloud. However it can be easily configured via the 
sensesagent.conf file to upload metrics to a different service. The format of the 
data sent can also be easily modified through the data template files. 

Installation
==============

Warnings


Warning

Pillow and PIL cannot co-exist in the same environment. Before installing Pillow, please uninstall PIL.

Warning

Pillow >= 1.0 no longer supports "import Image". Please use "from PIL import Image" instead.

Warning

Pillow >= 2.1.0 no longer supports "import _imaging". Please use "from PIL.Image import core as _imaging" instead.

  $ cd /usr/ports/graphics/py-pillow && make install clean


Configuration
====================

Configuration is done through conf/sensesagent.conf. 
"""
