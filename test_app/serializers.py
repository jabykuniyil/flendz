from rest_framework import serializers
from .models import Mark, Student

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = ('__all__')
        
class MarkSerializer(serializers.ModelSerializer):
    
    Student = StudentSerializer(read_only=True)
    class Meta:
        model = Mark
        fields = ('__all__')