from django.http import HttpRequest, HttpResponse
from .models import Enchere
from .serializer import EnchereSerializer
from rest_framework import generics

class EnchereDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enchere.objects.all()
    serializer_class = EnchereSerializer
    
class EnchereList(generics.ListCreateAPIView):
    queryset = Enchere.objects.all()
    serializer_class = EnchereSerializer