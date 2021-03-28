from django.db import models
from accounts.models import Branch,PaymentProfile,MyUser
class PaperboyProfile(models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE,related_name='pprofile')
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='branch_paperboy')
    payment_profile = models.OneToOneField(PaymentProfile,on_delete=models.CASCADE)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.pincode+'  '+self.name
class PaperboyDailyReport(models.Model):
    pprofile = models.ForeignKey(PaperboyProfile,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    total_papers = models.IntegerField()
    total_users = models.IntegerField()
    deliveried_papers = models.IntegerField(blank=True,null=True)
    deliveried_users = models.IntegerField(blank=True,null=True)



