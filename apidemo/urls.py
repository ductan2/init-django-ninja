from django.urls import path,include
from apidemo.routers.api import api
from admin_argon import admin
urlpatterns = [
    path('admin/', admin.admin.sites.site.urls),
    path('api/', api.urls),

]
