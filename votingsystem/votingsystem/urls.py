from django.urls import path
from voting.views import home_view, vote_view, results_view, add_candidate_view, edit_candidate_view, delete_candidate_view

urlpatterns = [
    path('', home_view, name='home'),
    path('vote/', vote_view, name='vote'),
    path('results/', results_view, name='results'),
    path('add-candidate/', add_candidate_view, name='add_candidate'),
    path('edit-candidate/<int:candidate_id>/', edit_candidate_view, name='edit_candidate'),
    path('delete-candidate/<int:candidate_id>/', delete_candidate_view, name='delete_candidate'),
]

