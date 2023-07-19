from django.contrib import admin
from  .models import DashboardModel, UserModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(DashboardModel)
