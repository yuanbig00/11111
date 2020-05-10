from django.urls import path
from django.conf.urls import url,include
from django.urls import include
from login import views
app_name='login'
urlpatterns = [
    # path('table/', views.table),
    # path('spread/', views.spread),
    # path('remark/', views.remark),
    # path('people/', views.people),
    path('search_result/', views.search_result,name='search_result'),
    path('search_form/', views.search_form,name='search_form'),
    path('login/', views.login,name='login'),
    path('index/', views.index,name='index'),
    path('index1/', views.index,name='index1'),
    url(r'^table/(?P<id>[0-9]+)$', views.table, name='table'),
    url(r'^spread/(?P<id>[0-9]+)$', views.spread, name='spread'),
    url(r'^remark/(?P<id>[0-9]+)$', views.remark, name='remark'),
    url(r'^people/(?P<id>[0-9]+)$', views.people, name='people'),
]