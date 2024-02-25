from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name='login_page'),
    path("upload/", views.upload_page, name='upload'),
    path("query/", views.query_page, name='query'),
    path("users/", views.user_page, name='users'),
    path("query/result/", views.query_result)
]
