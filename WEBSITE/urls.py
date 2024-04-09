from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('login_user/<str:user_group>/', views.login_user , name = 'login_user'),
    path('logout_user/', views.logout_user , name = 'logout_user'),
    path('upload/', views.upload_image, name='upload_image'),
    
    
    path('add_non_record/',views.add_non_record , name ='add_non_record'),
    path('add_student_record/',views.add_student_record , name ='add_student_record'),
    
    
    path('new_user/',views.new_user , name ='new_user'),
    path('register/', views.register, name='register'),
    
    
    path('get_students_data/', views.get_students_data, name='get_students_data'), 
    path('filter_student_records/',views.filter_student_records,name='filter_student_records'),
    
    
    
    
    
    path('get_details/', views.get_details, name='get_details'), 
]