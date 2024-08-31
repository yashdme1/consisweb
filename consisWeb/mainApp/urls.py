from django.urls import path
from .views import signup_view, login_view, logout_view ,home_view
from django.http import HttpResponse  
# urlpatterns = [
#     path('signup/', signup_view, name='signup'),
#     # Add a path for the success page (optional)
#     path('signup/success/', lambda request: HttpResponse('Signup successful!'), name='signup_success'),
#     path('login/', login_view, name='login'),
#      path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
#     path('', home_view, name='home'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('departments/', views.department_list, name='department_list'),
]