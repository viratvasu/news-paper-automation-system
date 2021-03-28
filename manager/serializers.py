from rest_framework import serializers
from .models import ManagerProfile
from accounts.serializer import BranchSerializer
class ManagerProfileSeriizer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)
    class Meta:
        model= ManagerProfile
        fields = ['branch','name','pno','id']