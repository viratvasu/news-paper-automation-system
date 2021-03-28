from rest_framework import serializers,fields
from .models import PaperboyProfile
class PaperboyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperboyProfile
        fields =['salary','name','pincode','id']