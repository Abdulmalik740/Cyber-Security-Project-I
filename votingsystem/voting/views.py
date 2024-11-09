from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Candidate, Vote
from .forms import VoteForm

def home_view(request):
    candidates = Candidate.objects.all()
    return render(request, 'voting/home.html', {'candidates': candidates})

def vote_view(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('results')
    else:
        form = VoteForm()
    return render(request, 'voting/vote.html', {'form': form})

def results_view(request):
    votes = Vote.objects.values('candidate__name').annotate(total=models.Count('candidate'))
    return render(request, 'voting/results.html', {'votes': votes})

def add_candidate_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Candidate.objects.create(name=name)
            return redirect('home')
    return render(request, 'voting/add_candidate.html')

def edit_candidate_view(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            candidate.name = name
            candidate.save()
            return redirect('home')
    return render(request, 'voting/edit_candidate.html', {'candidate': candidate})

def delete_candidate_view(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    if request.method == 'POST':
        candidate.delete()
        return redirect('home')
    return render(request, 'voting/delete_candidate.html', {'candidate': candidate})

