from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_content/', views.add_content),
    path('delete_content/<int:content_id>/', views.delete_content),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
   
]