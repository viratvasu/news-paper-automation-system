from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from accounts.serializer import MonthlyBillSerializer
from customer.serializers import PaperboyProfileSerializer
class getSalaries(APIView):
    def get(self,request):
        paperboy = request.user.pprofile.payment_profile
        bills = paperboy.monthly_bills.all()
        serializer = MonthlyBillSerializer(bills,many=True)
        return Response(serializer.data)
class getUsersPapers(APIView):
    def get(self,request):
        profile = request.user.pprofile
        customers = profile.customers.all()
        serializer = PaperboyProfileSerializer(customers,many=True)
        return Response(serializer.data)

class getInfo(APIView):
    def get(self,request):
        customer = request.user.pprofile
        return Response({'name':customer.name,'branch':customer.branch.name})


