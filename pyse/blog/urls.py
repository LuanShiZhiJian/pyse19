from django.urls import path
from . import views

urlpatterns = [
    path('list', views.index),
    path('detail/<int:post_id>',views.detail,name='detail')
]
