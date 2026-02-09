
from django.urls import path
from .views import signup_view, UserLoginView, UserLogoutView
from .views import profile_view, update_profile_view, change_password_view, booking_history_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    path('update_profile/', update_profile_view, name='update_profile'),
    path('change_password/', change_password_view, name='change_password'),
    path('booking_history/', booking_history_view, name='booking_history'),
]
