from django.urls import path

from . import views

app_name = 'StratBook'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('maps/<int:pk>/', views.MapDetailView.as_view(), name="maps"),
]
