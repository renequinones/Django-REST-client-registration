from django.urls import include, path, re_path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^shop/$', views.clients_list),
    re_path(r'^shop/(?P<pk>[0-9]+)$', views.clients_CRUD),

]
