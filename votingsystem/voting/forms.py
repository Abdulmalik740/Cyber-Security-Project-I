from django import forms
from .models import Vote

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['candidate', 'voter_id']

