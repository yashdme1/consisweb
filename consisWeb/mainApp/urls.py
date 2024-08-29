from django.urls import path
from .views import signup_view, login_view, logout_view ,home_view
from django.http import HttpResponse  
urlpatterns = [
    path('signup/', signup_view, name='signup'),
    # Add a path for the success page (optional)
    path('signup/success/', lambda request: HttpResponse('Signup successful!'), name='signup_success'),
    path('login/', login_view, name='login'),
     path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
]
