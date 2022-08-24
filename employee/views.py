from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from employee import models
from employee import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model


from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.contrib.auth import logout

from django.db.models import Q

def logout_view(request):
	logout(request)
	return redirect('login')


class EmployeeListView(LoginRequiredMixin,ListView):
	login_url = reverse_lazy('login')
	model = models.EmployeeModel
	context_object_name = 'employees_list'
	template_name = 'employee_list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		sq = self.request.GET.get("search_query")
		search_type = self.request.GET.get("search_type")

		if sq is not None:
			if search_type == "name":
				qs = qs.filter(Q(name__icontains=sq))
			elif search_type == "email":
				qs = qs.filter(Q(email__icontains=sq))
			elif search_type == "phone":
				qs = qs.filter(Q(phone__icontains=sq))
		return qs

class EmployeeCreateView(LoginRequiredMixin,CreateView):
	login_url = reverse_lazy('login')
	model = models.EmployeeModel
	success_url = reverse_lazy("employee_list")
	form_class = forms.EmployeeCreateForm
	template_name = 'employee_create.html'

class EmployeeUpdateView(SuperuserRequiredMixin,LoginRequiredMixin,UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("employee_list")
	model = models.EmployeeModel
	form_class = forms.EmployeeUpdateForm
	context_object_name = "employee"
	template_name = 'employee_update.html'

class EmployeeDeleteView(SuperuserRequiredMixin,LoginRequiredMixin,DeleteView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("employee_list")
	model = models.EmployeeModel
	context_object_name = "employee"
	template_name = 'employee_delete.html'

class EmployeeDetailView(LoginRequiredMixin,DetailView):
	login_url = reverse_lazy('login')
	model = models.EmployeeModel
	context_object_name = "employee"
	template_name = 'employee_detail.html'