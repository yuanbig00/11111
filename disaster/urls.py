from django.contrib import admin
from django.urls import path
from django.urls import include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('login/', include('login.urls',namespace='login')),
    path('register/', views.register),
    path('logout/', views.logout),
    path('table/', views.table),
    path('remark/', views.remark),
    path('spread/', views.spread),
    path('people/', views.people),
    path('captcha/', include('captcha.urls'))   # 增加这一行
]