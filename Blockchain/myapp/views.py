from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def users_page(request):
    return render(request, 'myapp/users.html')
