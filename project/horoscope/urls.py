from django.urls import path
from . import views


urlpatterns = [
    path('', views.horoscope_index_menu, name='horoscope_index'),
    path('<horoscope_get>/', views.horoscope_check_f, name='horoscope-names'),
]