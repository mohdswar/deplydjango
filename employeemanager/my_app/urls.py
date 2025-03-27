from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('employees/', views.employee_index, name='employee-index'),
    path('employees/<int:employee_id>/', views.employee_detail, name='employee-detail'),
    path('employees/create/', views.EmployeeCreate.as_view(), name='employee-create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdate.as_view(), name='employee-update'),
    path('employees/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employee-delete'),
    path('employees/<int:employee_id>/add-task/', views.add_task, name='add-task'),
    path('employees/<int:employee_id>/associate-role/<int:role_id>/', views.associate_role, name='associate-role'),
    path('employees/<int:employee_id>/remove-role/<int:role_id>/', views.remove_role, name='remove-role'),
    path('roles/create/', views.RoleCreate.as_view(), name='role-create'),
    path('roles/<int:pk>/', views.RoleDetail.as_view(), name='role-detail'),
    path('roles/', views.RoleList.as_view(), name='role-index'),
    path('roles/<int:pk>/update/', views.RoleUpdate.as_view(), name='role-update'),
    path('roles/<int:pk>/delete/', views.RoleDelete.as_view(), name='role-delete'),
    path('accounts/signup/', views.signup, name='signup'),
]