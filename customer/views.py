from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Subscription,CustomerDailyReport
from accounts.serializer import NewsPaperSerializer,MonthlyBillSerializer,PaymentProfileSerializer
from customer.serializers import CustomerDailyReportSerializer
from accounts.models import NewsPaper
class SubscriptionView(APIView):
    def get(self,request):
        customer = request.user.cprofile
        sub_amount = customer.subscription.amount    
        papers = customer.subscription.papers.all()
        papers_serializer = NewsPaperSerializer(papers ,many=True)
        return Response({'papers':papers_serializer.data,'amount':sub_amount},status=status.HTTP_200_OK)
    def post(self,request):
        paper_obj = NewsPaper.objects.get(id=request.data.get('id'))
        customer = request.user.cprofile     
        subscription_obj = customer.subscription
        subscription_obj.papers.add(paper_obj)
        subscription_obj.amount = subscription_obj.amount + int(paper_obj.price)
        subscription_obj.save()
        return Response({'detail':'Added to Subscription'},status=status.HTTP_201_CREATED)
class RemoveFromSubscription(APIView):
    def delete(self,request,pk):
        paper_obj = NewsPaper.objects.filter(id=pk).first()
        if paper_obj:
            customer = request.user.cprofile
            subscription_obj = customer.subscription
            if paper_obj in subscription_obj.papers.all():  
                subscription_obj.papers.remove(paper_obj)
                subscription_obj.amount = subscription_obj.amount - paper_obj.price
                subscription_obj.save()
                return Response({'detail':'Removed from Subscription'},status=status.HTTP_201_CREATED)
            else:
                return Response({'detail':'Not Found In your Subscription'},status=status.HTTP_400_BAD_REQUEST)
        else:
                return Response({'detail':'Paper Not Found'},status=status.HTTP_400_BAD_REQUEST)
# class GetPapers(APIView):
#     def get(self,request):
class GetPapers(APIView):
    def get(self,request):
        user_papers = request.user.cprofile.subscription.papers.all()
        newspapers = NewsPaper.objects.exclude(id__in = user_papers)
        serializer = NewsPaperSerializer(newspapers,many = True)
        return Response(serializer.data)
class DailyReportView(APIView):
    def get(self,request):
        customer_profile_obj = request.user.cprofile
        reports = customer_profile_obj.customer_reports.all().filter(is_received=True)
        serializer = CustomerDailyReportSerializer(reports,many=True)
        return Response(serializer.data)
    def post(self,request):
        customer_profile_obj = request.user.cprofile
        # daily_report_obj = CustomerDailyReport.objects.create(profile = customer_profile_obj)
        # daily_report_obj.save()
        return Response({'detail':'Create Daily Report'})

class BillInfo(APIView):
    def get(self,request):
        customer_profile = request.user.cprofile.payment_profile
        paid_bills = customer_profile.monthly_bills.filter(is_paid = True)
        paid_bills_serializer = MonthlyBillSerializer(paid_bills,many=True)
        pending_bills = customer_profile.monthly_bills.filter(is_paid = False)
        pending_bills_serializer = MonthlyBillSerializer(pending_bills,many=True)
        return Response({'paid':paid_bills_serializer.data,'pending':pending_bills_serializer.data})
    def put(self,request):
        customer_profile = request.user.cprofile.payment_profile
        serializer = PaymentProfileSerializer(customer_profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PayBill(APIView):
    def post(self,request,pk):
        customer_bill = request.user.cprofile.payment_profile.monthly_bills.filter(id=pk)[0]
        print(customer_bill)
        if(customer_bill):
            customer_bill.is_paid = True
            customer_bill.save()
        return Response({'detail':'success'})

class PaymentDetails(APIView):
    def get(self,request):
        customer_payment_profile = request.user.cprofile.payment_profile
        serializer = PaymentProfileSerializer(customer_payment_profile)
        return Response(serializer.data)
class ChangeUserName(APIView):
    def post(self,request):
        customer_profile = request.user.cprofile
        customer_profile.name = request.data.get('name')
        customer_profile.save()
        return Response(request.data.get('name'))

class ChangePassword(APIView):
    def post(self,request):
        user=request.user
        if(user.check_password(request.data.get('old'))):
            user.set_password(request.data.get('new'))
            user.save()
            return Response({'detail':'succesfull'})
        return Response({'detail':'Wrong Password'},status=status.HTTP_400_BAD_REQUEST)

class getInfo(APIView):
    def get(self,request):
        customer = request.user.cprofile
        return Response({'name':customer.name,'branch':customer.branch.name})