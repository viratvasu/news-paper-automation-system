from django.db import models
from accounts.models import Branch,MyUser

class ManagerProfile(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE,related_name='mprofile')
    branch = models.OneToOneField(Branch,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pno = models.CharField(max_length=10)

# class ManagerDailyReport(models.Model):
#     profile = models.ForeignKey(ManagerProfile,on_delete=models.CASCADE)


