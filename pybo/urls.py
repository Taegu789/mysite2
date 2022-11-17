from django.urls import path

from . import views
# 여기서 .의 의미는?

urlpatterns = [
    path('',views.index),
]
