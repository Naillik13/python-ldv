from shopping.views import Index, Details, Cart
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view()),
    path('<int:id>', Details.as_view()),
    path("basket", Cart.as_view(), name="cart"),

    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),
]
