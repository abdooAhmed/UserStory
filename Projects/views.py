# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from UserStoryApp.models import Project
from .forms import AddProjectsForm
from django.contrib.auth.decorators import login_required
from .filter import ProjectsFilter
# Create your views here.


@login_required
def Projects_list(request):
    project = Project.objects.all()
    my_filter = ProjectsFilter(request.GET, queryset=project)
    project = my_filter.qs
    return render(request, 'projects/projects.html', {'projects': project, 'filter': my_filter})


@login_required
def add_Projects(request):
    if request.method == 'POST':
        print('done')
        form = AddProjectsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = Project.objects.create(
                name=cd['name'], status=cd['status'], Business=cd['business'], User=request.user)
            if user is not None:
                return redirect('/Projects/list/')
    else:
        form = AddProjectsForm()
    print(form)
    return render(request, 'projects/addProject.html', {'form': form})


@login_required
def projectDetails(request, id):
    if request.method == 'POST':
        form = AddProjectsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            project = Project.objects.get(id=id)
            project.name = cd['name']
            project.status = cd['status']
            project.Business = cd['business']
            project.save()
            if project is not None:
                return redirect('/Projects/list/')
    else:
        project = Project.objects.get(id=id)
        form = AddProjectsForm(
            initial={'name': project.name, 'status': project.status, 'business': project.Business})
    return render(request, 'projects/projectDetails.html', {'form': form})
