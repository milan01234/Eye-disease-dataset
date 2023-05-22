from django.urls import path
from . import views
app_name="app"
urlpatterns=[
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('index',views.index,name="index"),
    
]