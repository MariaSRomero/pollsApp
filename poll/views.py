from django.shortcuts import get_object_or_404, redirect, render
import json
from.models import Choise, Question
# Create your views here.

def home(request):
    questions = Question.objects.all()
    return render(
        request,
        'poll/home.html',
        {
            "questions": questions
        })
def vote(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    if request.method == "POST":
        try:
            choice_id = request.POST.get('choice')
            choice = q.choise_set.get(pk=choice_id)
            choice.votes += 1
            choice.save()
            return redirect('poll:result', q_id)
        except (KeyError, Choise.DoesNotExist):
            return render(request,'poll/vote.html', {
                "question":q,
                "error_message": "Debes elegir algo!"
            })
    return render(request, 'poll/vote.html',{
        "question": q,
    })

def result(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    choices = q.choise_set.all()
    choice_text = json.dumps([choice.choise_text for choice in choices])
    votes = json.dumps([choice.votes for choice in choices])

    return render (request, 'poll/result.html', {
        "question": q,
        "choice_text": choice_text,
        "votes": votes,
    })