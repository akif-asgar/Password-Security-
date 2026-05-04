from django.urls import path
from .views import PasswordProcessView, RainbowChallengeView

urlpatterns = [
    path("process-password/", PasswordProcessView.as_view()),
    path("rainbow-challenge/", RainbowChallengeView.as_view()),
    
]