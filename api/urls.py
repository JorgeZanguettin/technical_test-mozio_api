from django.urls import path
from . import views

urlpatterns = [
    path('providers/', views.providers_list, name='providers_api'),
    path('provider/<int:pk>/', views.providers_detail),
    path('provider/<int:pk>/polygons/', views.providers_polygons_list),

    path('polygons/', views.polygons_list, name='polygons_api'),
    path('polygon/<str:_id>/', views.polygons_detail),

    path('polygons/<str:coord>/', views.polygons_list_by_coord)
]
