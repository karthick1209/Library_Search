from django.shortcuts import render
from .models import Library
from rest_framework import viewsets
from .serializers import LibraryDetailSerializer
# Create your views here.

class retrive_view(viewsets.ModelViewSet):
    queryset=Library.objects.all()
    serializer_class=LibraryDetailSerializer
    
    
    # def get_object(self):
    #     queySet=self.filter_queryset(self.get_queryset())
    #     obj=queySet.get(pk=self.request.user.Library_id)
    #     self.obj_permission(self.request,obj)
    #     return obj
    # return render(request,'index.html',{'Library':library})