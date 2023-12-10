from django.urls import path, include
from dashboard import views, models

app_name = 'dashboard'

urlpatterns = [

    path('', views.DashboardView.as_view(), name='dashboard'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('candidate/', include('candidate_management.urls')),
]
