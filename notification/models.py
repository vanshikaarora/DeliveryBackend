from django.db import models

# Create your models here.
class fcm_info(models.Model):
    fcm_token = models.CharField(max_length=400)

    def __str__(self):
        return self.fcm_token


class Users(models.Model):
    phone_no=models.CharField(max_length=10, primary_key=True)
    password=models.CharField(max_length=16)

    def __str__(self):
        return self.phone_no


class verify_user(models.Model):
    phone_no = models.ForeignKey(Users, on_delete=models.CASCADE, max_length=10)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.password