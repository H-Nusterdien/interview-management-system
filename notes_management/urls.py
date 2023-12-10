from django.urls import path
from notes_management import views


app_name = 'notes_management'

urlpatterns = [
    path('create/', views.CreateNoteView.as_view(), name='create-candidate-note'),
    path('<int:id>/', views.ManageNoteView.as_view(), name='manage-candidate-note'),
    path('<int:id>/update', views.UpdateNoteView.as_view(), name='update-candidate-note'),
    path('<int:id>/delete', views.DeleteNoteView.as_view(), name='delete-candidate-note'),
]
