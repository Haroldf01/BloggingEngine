from django.urls import path
from . import views

urlpatterns = [
    path('', views.BloggerList.as_view()),
    path('<int:pk>/', views.BlogDetail.as_view()),
]
