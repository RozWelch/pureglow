from . import views
from django.urls import path
from .views import HowToDetail

urlpatterns = [
    path("", views.HowToList.as_view(), name="skincare_articles"),
    path('add/', views.add_article, name='add_article'),
    # path('edit/<int:product_id>/', views.edit_article, name='edit_article'),
    # path('delete/<int:product_id>/', views.delete_article, name='delete_article'),
    path('<slug:slug>/', views.HowToDetail.as_view(), name='howto_detail'),
]
