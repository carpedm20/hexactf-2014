from django.shortcuts import render

from .models import Account

# Create your views here.
def sign_in(request):
    form = AccountAuthForm(data=request.POST)
    template = 'account/sign_in.html'

    if request.method == 'POST':
        if form.is_valid():
            # Success
            login(request, form.get_user())
            next_url = request.POST.get("next_url", "/")

            return redirect('/')
        else:
            # Failure
            return sign_in_view(request)

    return sign_in_view(request)

##############################
# Sign in View (Log in View)
##############################

def sign_in_view(request):
    form = AccountAuthForm(request.POST or None)
    template = 'account/sign_in.html'

    s = random.choice(say.keys())

    return render(request, template, {'form': form})


########################
# Sign up (Join)
########################

def sign_up(request):
    template = 'problem/view_problem.html'

    if request.method == 'POST':
        form = AccountCreateForm(request.POST)
        if form.is_valid():
            # `commit=False`: before save it to database, just keep it in memory
            username = form.clean_username()
            password = form.clean_password2()
            new_user = form.save()
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect("/")
    else:
        form = AccountCreateForm()

    return render(request, template,  {'form': form})

########################
# Sign out (Log out)
########################

@login_required
def sign_out(request):
    logout(request)
    #messages.success(request, 'You have successfully logged out.')
    return redirect('/')

