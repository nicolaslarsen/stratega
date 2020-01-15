from django.urls import path

from . import views

app_name = 'StratBook'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('map/add/', views.CreateMapView.as_view(), name="add_map"),
    path('map/<int:pk>/', views.MapDetailView.as_view(), name="map"),
    path('map/<int:pk>/delete/', views.DeleteMapView.as_view(), name="delete_map"),
    path('map/<int:pk>/strat/add/', views.create_strat_view, name="add_strat"),
    path('nadebook/', views.NadeIndexView.as_view(), name='nadebook'),
    path('map/<int:pk>/nades/', views.NadeMapDetailView.as_view(), name='nadeMap'),
    path('nade/<int:pk>/', views.NadeDetailView.as_view(), name="nade"),
    path('nade/<int:pk>/edit', views.NadeUpdateView.as_view(), name="update_nade"),
    path('nade/<int:pk>/delete', views.NadeDeleteView.as_view(), name="delete_nade"),
    path('map/<int:pk>/nades/add', views.NadeCreateView.as_view(), name='add_nade'),
    path('strat/<int:pk>/', views.StrategyDetailView.as_view(), name="strat"),
    path('strat/<int:pk>/edit/', views.update_strat_view, name="update_strat"),
    path('strat/<int:pk>/delete/', views.DeleteStrat.as_view(), name="delete_strat"),
]
