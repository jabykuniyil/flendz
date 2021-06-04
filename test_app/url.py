from django.urls import path
from .import views

urlpatterns = [
    path('student/', views.Students.as_view(), name = 'students'),
    path('student/add-mark/', views.Marks.as_view(), name = 'mark'),
    path('student/results/', views.Results.as_view(), name= 'results')
]