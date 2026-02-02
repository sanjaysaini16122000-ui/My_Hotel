from django.urls import path
from .views import add_review

urlpatterns = [
    path('add/<int:room_id>/', add_review, name='add_review'),
]
