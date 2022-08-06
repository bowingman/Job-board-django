from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicationList.as_view()),
    path('<int:pk>', views.ApplicationDetail.as_view()),
]
