from rest_framework.views import APIView
from .serializers import StudentSerializer
from django.http.response import JsonResponse
from .models import Student
from django.http.response import Http404
from rest_framework.response import Response

# Create your views here.

class StudentView(APIView):
    
    def get_student(self, pk):
        try:
            student = Student.objects.get(studentId=pk)
            return student
        except:
            return JsonResponse("Student does not Exists",safe=False)
    def get(self, request, pk=None):
        if pk:
            data = self.get_student(pk)
            serializer = StudentSerializer(data)
        else :
            data = Student.objects.all()
            serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)  
    
    def post(self, request):
        data = request.data 
        serializer = StudentSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student created successfully", safe=False)
        return JsonResponse("Failed to add Student", safe=False)
    
    def put(self, request, pk=None):
        Student_to_update = Student.objects.get(StudentId=pk)
        serializer = StudentSerializer(instance=Student_to_update, data=request.data, partial=True)
        
        if serializer.is_valid():
            return JsonResponse("Student Updated successfully", safe=False)
        return JsonResponse("Failed to update Student")
    
    def delete(self,request, pk=None):
        Student_to_delete = Student.objects.get(StudentId=pk)
        Student_to_delete.delete()   
        return JsonResponse("Student Deleted Successfully", safe=False) 
        
        