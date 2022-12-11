from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import AddUserForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from UserStoryApp.models import User, Project, Business, Role
from django.contrib.auth.decorators import login_required
from .filter import UsersFilter
# Create your views here.


@login_required
def user_list(request):
    User = get_user_model()
    users = User.objects.all()
    my_filter = UsersFilter(request.GET, queryset=users)
    users = my_filter.qs
    for u in users:
        project = Project.objects.filter(User=u)
        if len(project):
            u.project = project
    for u in users:
        business = Business.objects.filter(User=u)
        print(business)
        if len(business):
            u.business = business
            print(u.business)
        u.Role = Role(u.Role).name
    return render(request, 'user/users.html', {'users': users, 'filter': my_filter})


@login_required
def add_user(request):
    if request.method == 'POST':
        print('done')
        form = AddUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['username'], password=cd['password'],
                                            email=cd['email'], first_name=cd['first_name'], last_name=cd['last_name'], Role=cd['Role'])
            if user is not None:
                if user.is_active:
                    return redirect('/Users/list/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = AddUserForm()
    return render(request, 'user/addUser.html', {'form': form})


def userDetails(request, id):
    User = get_user_model()
    users = User.objects.get(id=id)
    form = AddUserForm(
        initial={'first_name': users.first_name, 'last_name': users.last_name, 'username': users.username, 'password': users.password,
                 'email': users.email, 'Role': (users.Role, Role(users.Role).name)})
    return render(request, 'user/userDetails.html', {'form': form})
