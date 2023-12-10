from django.urls import path, include
from candidate_management import views


app_name = 'candidate_management'

urlpatterns = [
    path('create/', views.CreateCandidateView.as_view(), name='create-candidate'),
    path('<int:id>/', views.ManageCandidateView.as_view(), name='manage-candidate'),
    path('<int:id>/update/', views.UpdateCandidateView.as_view(), name='update-candidate'),
    path('<int:id>/delete/', views.DeleteCandidateView.as_view(), name='delete-candidate'),
    path('<int:id>/note/', include('notes_management.urls', namespace='notes_management')),
]
