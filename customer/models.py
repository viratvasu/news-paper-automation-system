from django.db import models
from accounts.models import MyUser,NewsPaper,Adress,PaymentProfile,Branch
from paperboy.models import PaperboyProfile
class Subscription(models.Model):
    papers = models.ManyToManyField(NewsPaper)
    amount = models.IntegerField(default=0) 

    def __str__(self):
        return str(self.amount)
class CustomerProfile(models.Model):
    user            = models.OneToOneField(MyUser,on_delete=models.CASCADE,related_name='cprofile')
    paperboy        = models.ForeignKey(PaperboyProfile,on_delete=models.CASCADE,related_name='customers')
    name            = models.CharField(max_length=100)
    subscription    = models.OneToOneField(Subscription,on_delete=models.CASCADE)
    adress          = models.OneToOneField(Adress,on_delete=models.CASCADE)
    payment_profile = models.OneToOneField(PaymentProfile,on_delete=models.CASCADE)
    branch          = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='banch_user')
 
    def __str__(self):
        return self.name
class CustomerDailyReport(models.Model):
    profile         = models.ForeignKey(CustomerProfile,on_delete=models.CASCADE,related_name='customer_reports')
    is_received     = models.BooleanField(default=False)
    date            = models.DateTimeField(auto_now=True)
    amount          = models.IntegerField(blank=True,null=True)
    no_of_papers    = models.IntegerField(blank=True,null=True)







