from django.urls import path
from . import views


urlpatterns = [
    path('postRequest/', views.postRequest)
]
