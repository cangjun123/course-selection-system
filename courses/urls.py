from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('student/<str:student_id>/', views.student_detail, name='student_detail'),
    path('add_course/<str:student_id>/<int:course_id>/', views.add_course, name='add_course'),
    path('drop_course/<str:student_id>/<int:course_id>/', views.drop_course, name='drop_course'),
]
