from ninja_extra import api_controller, route


@api_controller('/task', tags=['Task'], permissions=[])
class TaskController:
    def __init__(self):
        print("TaskController Initialized")

    @route.get("/")
    def hello(self, request):
        return {"message": "Hello World"}

    @route.post("/")
    def create_task(self, request):
        return {"message": "Task Created"}
