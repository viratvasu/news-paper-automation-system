import random
import secrets
from django.db.models import Func,F
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from .models import MyUser,Adress,PaymentProfile
from paperboy.models import PaperboyProfile
from customer.models import CustomerProfile,Subscription
def create_adress(doorno,colony,landmark,village,mandal,pincode):
    try:
        address_obj = Adress.objects.create(doorno=doorno,colony=colony,landmarak=landmark,village=village,mandal=mandal,pincode=pincode)
        address_obj.save()
        return address_obj
    except Exception:
        return False
def create_payment_profile(card_no,cvv,month,year):
    try:
        payment_profile_obj = PaymentProfile.objects.create(card_no=card_no,cvv=cvv,month=month,year=year)
        payment_profile_obj.save()
        return payment_profile_obj
    except Exception:
        return False
class CreateCustomer(APIView):
    authentication_classes  = []
    permission_classes      = []
    def post(self,request):
        try:
            user_obj = MyUser.objects.create(email=request.data['email'],user_type='customer')
            user_obj.set_password(request.data['password'])
            user_obj.save()
            adress_obj = create_adress(doorno=request.data['doorno'],colony=request.data['colony'],landmark=request.data['landmark'],village=request.data['village'],mandal=request.data['mandal'],pincode=request.data['pincode'])
            if not(adress_obj):
                user_obj.delete()
                return Response({'detail':'Problem Faced with your adress'})
            payment_profile_obj = create_payment_profile(card_no=request.data['card_no'],cvv=request.data['cvv'],month=request.data['month'],year=request.data['year'])
            if not(payment_profile_obj):
                user_obj.delete()
                adress_obj.delete()
                return Response({'detail':'Problem Faced with your Payment Details'})
            paper_boy_obj = PaperboyProfile.objects.annotate(abs_diff=Func(F('pincode')-int(request.data['pincode']),function='ABS')).order_by('abs_diff').first()
            if not(paper_boy_obj):
                user_obj.delete()
                adress_obj.delete()
                payment_profile_obj.delete()
                return Response({'detail':'There are no Paperboys'})
            subscription_obj = Subscription.objects.create()
            try:
                customer_obj = CustomerProfile.objects.create(user=user_obj,paperboy=paper_boy_obj,name=request.data['name'],adress=adress_obj,payment_profile=payment_profile_obj,branch=paper_boy_obj.branch,subscription=subscription_obj)
                customer_obj.save()
                return Response({'detail':'created succesfuly'})
            except Exception as e:
                payment_profile_obj.delete()
                user_obj.delete()
                adress_obj.delete()
                return Response({'detail':'Problem While creating your Account'})
        except Exception as e:
            if 'email' in str(e):
                return Response({'detail':'Email already exists'},status=status.HTTP_400_BAD_REQUEST)
            return Response({'detail':'sorry..Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
class getInfo(APIView):
    def get(self,request):
        user = request.user
        return Response({'user_type':user.user_type})

def id_generator(size=9, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_generator2(size=9, chars=string.digits):
    return ''.join(secrets.choice(chars) for _ in range(size))
