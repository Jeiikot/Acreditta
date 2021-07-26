from django.urls import path
from .views import PasswdFinderView

urlpatterns = [
    path('passwd/', PasswdFinderView.as_view(), name="passwd"),
]
