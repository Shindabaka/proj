from rest_framework import serializers
from .models import *

class studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = ('st_name','teacher')

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = ('subject_name','st_grade')