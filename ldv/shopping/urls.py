from shopping.views import Index, Details
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view()),
    path('<int:id>', Details.as_view()),
    path('login', auth_views.LoginView.as_view())
]
