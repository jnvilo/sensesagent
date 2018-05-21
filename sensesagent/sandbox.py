# -*- coding: utf-8 -*

from ConfigObject import ConfigObject



config = ConfigObject(filename = "config.ini")
config.section = dict(value=1)

config["server_url"] = "http://localhost:8000"


config.write()
print("completed")