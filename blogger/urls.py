from django.urls import path
from . import views

# NOTE app_name will help us do a reverse look-up latter
app_name = "articles"

urlpatterns = [
    path('', views.BloggerView.as_view()),
    path('<int:pk>', views.BloggerView.as_view()),
    path('users', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view())
]
