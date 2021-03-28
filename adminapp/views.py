from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from manager.serializers import ManagerProfileSeriizer
from manager.models import ManagerProfile
from accounts.models import Branch,MyUser,NewsPaper
from accounts.serializer import NewsPaperSerializer
class Branches(APIView):
    def get(self,request): 
        managers = ManagerProfile.objects.all()
        serializer = ManagerProfileSeriizer(managers,many=True)
        return Response(serializer.data)
    def post(self,request):
        branch_obj = Branch.objects.create(name=request.data['name'])
        branch_obj.save()
        user_obj = MyUser.objects.create(email=request.data['email'],user_type='customer')
        user_obj.set_password(request.data['password'])
        user_obj.save()
        manager_obj = ManagerProfile.objects.create(user=user_obj,branch=branch_obj,name=request.data['mname'])
        manager_obj.save()
        return Response({'detail':'Created Succesfully'})
class BranchDetail(APIView):
    def delete(self,request,pk):
        manager_obj = ManagerProfile.objects.get(id=pk)
        manager_obj.delete()
        return Response({'detail':'deleted succesfully'})

class Newspapers(APIView):
    def get(self,request):
        newspapers = NewsPaper.objects.all()
        serializer = NewsPaperSerializer(newspapers,many=True)
        return Response(serializer.data)
    def post(self,request):
        news_paper_obj = NewsPaper.objects.create(image=request.data['image'],title=request.data['title'],price=request.data['price'])
        news_paper_obj.save()
        return Response({'detail':'Created'})
class NewsPaperDetail(APIView):
    def delete(self,request,pk):
        news_paper_obj = NewsPaper.objects.get(id=pk)
        news_paper_obj.delete()
        return Response({'detail':'deleted succesfully'})