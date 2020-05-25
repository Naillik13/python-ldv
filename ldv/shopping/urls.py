from shopping.views import Index, Details
from django.urls import path

urlpatterns = [
    path('', Index.as_view()),
    path('<int:id>', Details.as_view()),
]
