from pecanrest.controllers import order

class ApiController(object):
    orders = order.OrdersController()
