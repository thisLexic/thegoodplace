from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'ingredients_list/', views.ingredients_list),
    url(r'ingredients_detail/', views.ingredients_list),
    url(r'ingredients_update_form/', views.ingredients_list),
    url(r'ingredients_create_form/', views.ingredients_list),

    url(r'recipes_list/', views.ingredients_list),
    url(r'recipes_detail/', views.ingredients_list),
    url(r'recipes_update_form/', views.ingredients_list),
    url(r'recipes_create_form/', views.ingredients_list),

    url(r'orders_list/', views.ingredients_list),
    url(r'orders_detail/', views.ingredients_list),
    url(r'orders_update_form/', views.ingredients_list),
    url(r'orders_create_form/', views.ingredients_list),
]