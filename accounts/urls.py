# accounts/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
             template_name='accounts/login.html'
         ),
         name='login'),

    path('logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),

    path('agents/',      views.agent_list,   name='agent_list'),
    path('agents/new/',  views.agent_create, name='agent_create'),
]


# # accounts/urls.py
#
# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views
#
# urlpatterns = [
#     path('login/',  auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('agents/', views.agent_list, name='agent_list'),
#     path('agents/new/', views.agent_create, name='agent_create'),
# ]