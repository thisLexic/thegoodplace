from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'ingredients_list/', views.ingredients_list)
]