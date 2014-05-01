from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Problem
from .forms import ProblemCreateForm
from account.models import Account

from utils.func import *

# Create your views here.
@login_required
def view_problem(request):
    template = 'problem/view_problem.html'
    current_account = get_account_from_user(request.user)

    problems = Problem.objects.all()

    for problem in problems:
        if problem in current_account.solved_problems:
            problem.solved = True
        else:
            problem.solved = False

    return render(request, template, {'problems': problems})

@login_required
def create_problem(request):
    template = 'problem/create_problem.html'

    if request.method == 'POST':
        form = ProblemCreateForm(request.POST, request.FILES)
        if form.is_valid():
            problem = form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProblemCreateForm()

    return render_to_response(template, {'form': form})
