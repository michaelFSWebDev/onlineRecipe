from django.shortcuts import render, redirect
from userApp.models import User as LoggedUser


# Create your views here.
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = LoggedUser.objects.get(id=request.session['user_id'])
    context = {
        'user' : user
    }
    return render (request, 'dashboard.html', context)
