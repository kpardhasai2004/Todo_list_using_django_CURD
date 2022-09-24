from django.urls import path
from . import views as authp_views
from todo import views as todo_views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',authp_views.home,name='home'),
    path('register/',authp_views.register,name='register'),
    path('profile/',authp_views.profile, name='profile'),
    path('accounts/profile/',todo_views.thome, name='afterlogin'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),

    path('todo/home/',todo_views.thome, name='thome' ),
    path('todo/upload/',todo_views.tupload, name='tupload'),
    path('todo/home/tdelete/<int:id>/',todo_views.tdelete,name='tdelete'),
    path('todo/home/tupdate/<int:id>/',todo_views.tupdate,name='tupdate'),
    path('todo/home/tcomp/<int:id>/',todo_views.tcomp,name='tcomp'),
    
    ]