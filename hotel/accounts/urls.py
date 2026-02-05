
from django.urls import path
from .views import signup_view, UserLoginView, UserLogoutView
from .views import profile_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
]
