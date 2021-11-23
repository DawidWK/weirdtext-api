
from django.urls import path
from api import views
urlpatterns = [
    path('encode/', views.Encode.as_view(), name="encode"),
]
