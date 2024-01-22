from django.contrib import admin
from aaaa import views
from django.urls import path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.my_view,name='home'),
    path('form', views.member_form,name='njj'),
]

