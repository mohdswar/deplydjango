from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Employee, Role
from .forms import TaskForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def employee_index(request):
    employees = Employee.objects.filter(user=request.user)
    return render(request, 'employees/index.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    task_form = TaskForm()
    
    available_roles = Role.objects.filter(user=request.user).exclude(id__in=employee.roles.all().values_list('id'))
    
    return render(request, 'employees/detail.html', { 
        'employee': employee,
        'task_form': task_form,
        'available_roles': available_roles
    })

class EmployeeCreate(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['name', 'description', 'age']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ['name', 'description', 'age']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EmployeeDelete(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = '/employees/'

def add_task(request, employee_id):
    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.employee_id = employee_id
        new_task.save()
        return redirect('employee-detail', employee_id=employee_id)

class RoleCreate(LoginRequiredMixin, CreateView):
    model = Role
    fields = ['name']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RoleList(LoginRequiredMixin, ListView):
    model = Role
    
    def get_queryset(self):
        return Role.objects.filter(user=self.request.user)

class RoleDetail(LoginRequiredMixin, DetailView):
    model = Role
    
    def get_queryset(self):
        return Role.objects.filter(user=self.request.user)

class RoleUpdate(LoginRequiredMixin, UpdateView):
    model = Role
    fields = ['name']
    
    def get_queryset(self):
        return Role.objects.filter(user=self.request.user)

class RoleDelete(LoginRequiredMixin, DeleteView):
    model = Role
    success_url = '/roles/'
    
    def get_queryset(self):
        return Role.objects.filter(user=self.request.user)

def associate_role(request, employee_id, role_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    role = get_object_or_404(Role, pk=role_id, user=request.user)
    employee.roles.add(role)
    return redirect('employee-detail', employee_id=employee.id)

def remove_role(request, employee_id, role_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    role = get_object_or_404(Role, pk=role_id, user=request.user)
    employee.roles.remove(role)
    return redirect('employee-detail', employee_id=employee.id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('employee-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)