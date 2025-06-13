from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *


class studentsAPI(generics.ListAPIView):
    queryset = students.objects.all()
    serializer_class = studentsSerializer

class subjectAPI(generics.ListAPIView):
    queryset = subject.objects.all()
    serializer_class = subjectSerializer