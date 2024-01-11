from django.shortcuts import render
from .models import Image

def home(request):
    searchTerm = request.GET.get('searchImage')
    if searchTerm:
        images= Image.objects.filter(imagename__icontains=searchTerm)
    else:
        images=Image.objects.all()
    return render(request, 'home.html',	{'searchTerm':searchTerm, 'images':images}) 

# views.py
 
from .models import Image
from .serializers import UploadedImage
from rest_framework.views import APIView 
from rest_framework import status
from rest_framework.response import Response
class Imageview(APIView):
    def get(self,request,*args,**kwargs):
        image = Image.objects.all()
        serializer =UploadedImage(image , context = {'request':request},many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
