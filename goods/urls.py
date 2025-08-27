from django.urls import path
from . import views

urlpatterns = [
    # path('catalog/', views.catalog_view, name='catalog'),
    path('', views.catalog_view, name='catalog'),
    path('<slug:category_slug>/', views.catalog_view, name='catalog_by_category'),
]