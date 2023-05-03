from . import views
from django.urls import path

urlpatterns = [
    path("", views.HowToList.as_view(), name="skincare_articles"),
    path('<slug:slug>/', views.howto_detail, name='howto_detail'),
]
