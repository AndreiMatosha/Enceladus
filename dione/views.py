from django.shortcuts import render
from dione.models import Employee, Company
from django.views.generic.list import ListView


# Create your views here.
def list_employees(request):
    context = {'employees': Employee.objects.all()}
    return render(request, template_name='dione/employees.html', context=context)


class CompanyList(ListView):
    model = Company
