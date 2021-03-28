from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from customer.models import CustomerProfile
from accounts.models import MonthlyBill
from paperboy.models import PaperboyProfile
def generatesalaries(paperboy_instance):
    bill_instance = MonthlyBill(amount = int(paperboy_instance.salary),payment_profile=paperboy_instance.payment_profile)
    bill_instance.save()
def generate_bills_for_users(customer_instance):
    print(customer_instance)
    subscription = customer_instance.subscription
    bill_instance = MonthlyBill(amount = int(subscription.amount)*30,payment_profile=customer_instance.payment_profile)
    bill_instance.save()
class GenerateBills(APIView):
    def post(self,request):
        profiles = CustomerProfile.objects.all()
        for i in profiles:
            generate_bills_for_users(i)
        return Response({'detail':'generated bills'})
class GenerateSalaries(APIView):
    def post(self,request):
        profiles = PaperboyProfile.objects.all()
        for i in profiles:
            generatesalaries(i)
        return Response({'detail':'generated salaries'})


