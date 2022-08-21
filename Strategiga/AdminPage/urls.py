from django.urls import path

from . import views

app_name = 'AdminPage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('updateuser/<int:pk>', views.UpdateUser, name='update_user'),
    path('swap_strategies/', views.SwapStrategies, name='swap_strategies'),
]
