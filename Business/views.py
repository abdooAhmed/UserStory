from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import AddProjectsForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from UserStoryApp.models import Business, BusinessCategory, Project
from django.contrib.auth.decorators import login_required
from .filter import BusinessFilter
# Create your views here.


@login_required
def business_list(request):
    Industry = ""
    Projects = ""
    business = Business.objects.all()
    my_filter = BusinessFilter(request.GET, queryset=business)
    business = my_filter.qs
    if request.GET.get("Industry"):
        business = business.filter(
            businessIndustry__name__contains=request.GET.get("Industry"))
        Industry = request.GET.get("Industry")
    if request.GET.get("Projects"):
        business = business.filter(
            project__name__contains=request.GET.get("Projects"))
        Projects = request.GET.get("Projects")
    for b in business:
        project = Project.objects.filter(Business=b)
        b.project = "\n".join([f'{p.name} , ' for p in project])
    return render(request, 'Business/Business.html', {'businesses': business, 'filter': my_filter, 'form': {'industry': Industry, 'projects': Projects}})


@login_required
def add_business(request):
    if request.method == 'POST':
        form = AddProjectsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            current_user = request.user
            user = Business.objects.create(hourlyRate=cd['hourlyRate'], name=cd['name'],
                                           LegalEntityName=cd['LegalEntityName'], Address=cd['Address'],
                                           BusinessNumber=cd['BusinessNumber'],
                                           BusinessEmail=cd['BusinessEmail'], User=current_user)
            user.businessIndustry.set(cd['businessIndustry'])
            print(user)
            if user is not None:
                return redirect('/Business/list/')
    else:
        form = AddProjectsForm()
    print(form)
    return render(request, 'Business/addBusiness.html', {'form': form})
