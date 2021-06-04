#importing rest_framework and it's libraries
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#importing serialized classes
from .serializers import StudentSerializer, MarkSerializer

#importing models from the same app
from .models import Student, Mark


# Create your views here.

class Students(APIView):
    
    #getting all Student's data
    def get(self, request):
        students = Student.objects.all()
        serializer_class = StudentSerializer(students, many=True)
        return Response(serializer_class.data)
    
    #creating a new Student
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class Marks(APIView):
    
    #getting the marks of all students
    def get(self, request):
        marks = Mark.objects.all()
        serializer_class = MarkSerializer(marks, many=True)
        return Response(serializer_class.data)
    
    #adding the mark to that particular student
    def post(self, request):
        mark = request.data['mark']
        roll_no = request.data['student']
        if Student.objects.filter(roll_no=roll_no).exists():
            Mark.objects.get_or_create(student_id=roll_no, mark=int(mark))
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

class Results(APIView):
    
    #getting the results by category based
    def get(self, request):
        results = {}
        marks_of_students = Mark.objects.all()
        total_students = Mark.objects.all().count()
        grade_A = 0
        grade_B = 0
        grade_C = 0
        grade_D = 0
        grade_E = 0
        grade_F = 0
        no_grade = 0
        for mark in marks_of_students:
            if mark.mark <= 100 and mark.mark >= 91:
                grade_A += 1
            elif mark.mark <= 90 and mark.mark >= 81:
                grade_B += 1
            elif mark.mark <= 80 and mark.mark >= 71:
                grade_C += 1
            elif mark.mark <= 70 and mark.mark >= 61:
                grade_D += 1
            elif mark.mark <= 60 and mark.mark >= 55:
                grade_E += 1
            elif mark.mark < 55:
                grade_F += 1
            else:
                no_grade += 1
        if total_students > 0:
            #percentage of students with distinction
            distinction = grade_A / total_students * 100
            #percentage of students with first class
            first_class = (grade_B + grade_C) / total_students * 100
            #percentage of students who are all passed
            passed_students = (total_students - grade_F) / total_students * 100
        else:
            return Response(status=status.)
        results['total_students'] = total_students
        results['grade_A'] = grade_A
        results['grade_B'] = grade_B
        results['grade_C'] = grade_C
        results['grade_D'] = grade_D
        results['grade_E'] = grade_E
        results['grade_F'] = grade_F
        results['no_grade'] = no_grade
        results['distinction'] = distinction
        results['first_class'] = first_class
        results['passed_students'] = passed_students
        return Response(results, status=status.HTTP_200_OK)
        
        