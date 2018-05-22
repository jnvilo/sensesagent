from configobj import ConfigObj
config = ConfigObj("sensesagent.conf")


print(config)
print(config["keyword1"])