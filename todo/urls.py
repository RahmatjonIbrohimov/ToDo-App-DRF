from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeApiViews.as_view(), name='home'),
    path('<int:pk>/', views.TDetailApiViews.as_view(), name='detail-page'),
    path('<int:pk>/update/', views.TUpdateApiViews.as_view(), name='update'),
    path('new/', views.TCreateApiViews.as_view(), name='create-page'),
    path('<int:pk>/delete/', views.TDeleteApiViews.as_view(), name='delete'),
]
