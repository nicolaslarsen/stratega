from django.urls import path

from . import views

app_name = 'StratBook'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('map/add/', views.CreateMapView.as_view(), name="add_map"),
    path('map/<int:pk>/', views.MapDetailView.as_view(), name="map"),
    path('map/<int:pk>/delete/', views.DeleteMapView.as_view(), name="delete_map"),
    path('map/<int:pk>/strat/add/', views.CreateStratView.as_view(), name="add_strat"),
    path('nadebook/', views.NadeIndexView.as_view(), name='nadebook'),
    path('map/<int:pk>/nades/', views.NadeMapDetailView.as_view(), name='nadeMap'),
    path('nade/<int:pk>/', views.NadeDetailView.as_view(), name="nade"),
    path('strat/<int:pk>/', views.StrategyDetailView.as_view(), name="strat"),
    path('strat/<int:pk>/edit/', views.UpdateStrat.as_view(), name="update_strat"),
    path('strat/<int:pk>/delete/', views.DeleteStrat.as_view(), name="delete_strat"),
]
