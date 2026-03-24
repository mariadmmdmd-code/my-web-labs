from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.main_page, name='main'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('login/', views.login_page, name='login'),
    path('login/css/', views.login_css, name='login_css'),
    path('login/js/', views.login_js, name='login_js'),
    path('send-feedback/', views.send_feedback, name='send_feedback'),
]