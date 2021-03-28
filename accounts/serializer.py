from rest_framework import serializers,fields
from .models import NewsPaper,MonthlyBill,PaymentProfile,Branch

class NewsPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPaper
        fields = '__all__'
class MonthlyBillSerializer(serializers.ModelSerializer):
    date = fields.DateTimeField(input_formats=['%Y-%m-%d'])
    class Meta:
        model = MonthlyBill
        exclude = ['payment_profile']
class PaymentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentProfile
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields='__all__'