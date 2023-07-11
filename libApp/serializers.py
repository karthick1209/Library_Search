
from libApp.models import Library
from rest_framework import serializers

# Create your models here.
class LibraryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields ='__all__'