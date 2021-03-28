from rest_framework import serializers
from .models import CustomerDailyReport,PaperboyProfile,Subscription
from accounts.serializer import NewsPaperSerializer
# class SubscriptionSerializer(serializers.ModelSerializer):
#     papers = NewsPaperSerializer(read_only = True,many=True)
#     class Meta:
#         model = Subscription
#         fields ='__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    papers = NewsPaperSerializer(many=True,read_only=True)
    class Meta:
        model = Subscription
        fields = '__all__'
class PaperboyProfileSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(read_only=True)
    class Meta:
        model = PaperboyProfile
        fields = ['name','subscription']
class CustomerDailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDailyReport
        exclude = ('profile',)
