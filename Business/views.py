from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import AddBusinessForm1, AddBusinessForm2
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
    if request.method == 'GET' and 'businessIndustry' in request.GET:
        BusinessCategory.objects.create(name=request.GET.get("Name"))
        form = AddBusinessForm1()
        form2 = AddBusinessForm2()
        return redirect('/Business/AddBusiness/')
    if request.method == 'POST':
        form = AddBusinessForm1(request.POST)
        form2 = AddBusinessForm2(request.POST)
        if form.is_valid() and form2.is_valid():
            cd = form.cleaned_data
            cd2 = form2.cleaned_data
            user = Business.objects.create(hourlyRate=cd['hourlyRate'], name=cd['name'],
                                           LegalEntityName=cd2['LegalEntityName'], Address=cd2['Address'],
                                           BusinessNumber=cd2['BusinessNumber'],
                                           BusinessEmail=cd2['BusinessEmail'], ABN=cd2['ABN'])
            user.businessIndustry.set(cd['businessIndustry'])
            users = []
            for u in cd['Customer']:
                users.append(u)
            for u in cd['Internal_User']:
                users.append(u)
            print(users)
            user.User.set(users)
            if user is not None:
                return redirect('/Business/list/')
        return render(request, 'Business/addBusiness.html', {'form': form, 'form2': form2})
    form = AddBusinessForm1()
    form2 = AddBusinessForm2()
    return render(request, 'Business/addBusiness.html', {'form': form, 'form2': form2})


def BusinessDetails(request, id):
    business = Business.objects.get(id=id)
    print(business.User.all())
    form = AddBusinessForm1(
        initial={'name': business.name, 'businessIndustry': business.businessIndustry.all(), 'hourlyRate': business.hourlyRate,
                 'Internal_User': business.User.filter(Role=2), 'Customer': business.User.filter(Role=1)})
    form2 = AddBusinessForm2(
        initial={'LegalEntityName': business.LegalEntityName, 'Address': business.Address,
                 'BusinessNumber': business.BusinessNumber, 'BusinessEmail': business.BusinessEmail, 'ABN': business.ABN})
    return render(request, 'Business/BusinessDetails.html', {'form': form, 'form2': form2})
