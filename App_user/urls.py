from django.urls import path, include
from . import views
# from ckeditor_uploader import views as uploader_views


urlpatterns = [
    path('', views.home, name='home'),
    path('password', views.password, name='password'),
    path('otp', views.otp, name='otp'),
    path('test', views.test, name='test'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    path("checkOtp/<str:pk>", views.checkOtp, name="checkOtp"),
    path("logout/<str:pk>", views.logoutEach, name="logout"),
    path("profile", views.profile, name="profile"),
]
