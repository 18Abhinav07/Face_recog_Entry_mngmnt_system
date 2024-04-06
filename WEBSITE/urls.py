from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('login_user/<str:user_group>/', views.login_user , name = 'login_user'),
    path('logout_user/', views.logout_user , name = 'logout_user'),
    path('upload/', views.upload_image, name='upload_image'),
    path('add_record/',views.add_record , name ='add_record'),
]