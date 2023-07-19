from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    user_img = models.ImageField(upload_to='user/')


class DashboardModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    qr_img = models.ImageField(upload_to='user-qr/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
