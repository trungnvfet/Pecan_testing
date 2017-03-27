#from pecanrest.controllers import v1

#class RootController(object):
#    v1 = v1.VersionController()
from pecanrest.controllers import api

class RootController(object):
    api = api.ApiController()
