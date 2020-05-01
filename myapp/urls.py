
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('reg/',views.reg,name='reg'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('upprofile/', views.updateprofile, name='updateprofile'),
    path('detail/<int:pk>',views.detailpost,name='detail'),
    path('add/',views.addpost,name='add'),
    path('my/',views.my,name='my'),
]


