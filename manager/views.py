from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from paperboy.serializer import PaperboyProfileSerializer
from paperboy.models import PaperboyProfile
from accounts.models import MyUser
from customer.models import CustomerDailyReport
from accounts.views import create_payment_profile
class Paperboys(APIView):
    def get(self,request):
        profile = request.user.mprofile
        paper_boys = profile.branch.branch_paperboy.all()
        serializer = PaperboyProfileSerializer(paper_boys,many=True)
        return Response(serializer.data)
    def post(self,request):
        try:
            user_obj = MyUser.objects.create(email=request.data['email'],user_type='customer')
            user_obj.set_password(request.data['password'])
            user_obj.save()
            paym_obj = create_payment_profile(request.data['card_no'],request.data['cvv'],request.data['month'],request.data['year'])
            paper_boy_obj = PaperboyProfile.objects.create(user=user_obj,name=request.data['name'],pincode=request.data['pincode'],salary=request.data['salary'],branch=request.user.mprofile.branch,payment_profile=paym_obj)
            paper_boy_obj.save()
            return Response({'detail':'created'})
        except Exception as e:
            print(e)
            return Response({'detail':'Something wen wrong'},status=status.HTTP_400_BAD_REQUEST)

class PaperBoysModify(APIView):
    def delete(self,request,pk):
        pp = PaperboyProfile.objects.get(id=pk)
        user = pp.user
        user.delete()
        return Response({'detail':'deleted succesfully'})
def generate_bills_for_users(customer_instance):
    subscription = customer_instance.subscription
    no_of_papers = len(subscription.papers.all())
    customer_instance = CustomerDailyReport(profile=customer_instance,is_received=True,amount=subscription.amount,no_of_papers=no_of_papers)
    customer_instance.save()
class Generate(APIView):
    def post(self,request):
        mprofile_branch = request.user.mprofile.branch
        users = mprofile_branch.banch_user.all()
        for i in users:
            generate_bills_for_users(i)
        return Response({'detail':'generated succesfully'})

class getInfo(APIView):
    def get(self,request):
        customer = request.user.mprofile
        return Response({'name':customer.name,'branch':customer.branch.name})



