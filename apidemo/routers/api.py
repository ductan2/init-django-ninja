from ninja_extra import NinjaExtraAPI
from apidemo.routers.task import TaskController
from apidemo.routers.product import ProductController

api = NinjaExtraAPI()

api.register_controllers(ProductController, TaskController)
