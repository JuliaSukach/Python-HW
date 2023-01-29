from django.urls import path
from django.urls import include

from .views import UserProfileCreateView
from .views import UserProfileDetailView

urlpatterns = [
    path('all-profile/', UserProfileCreateView.as_view(), name='all-profile'),
    path('profile/<int:pk>', UserProfileDetailView.as_view(), name='profile')
]