from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from department import models
from department import forms

from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from employee.models import EmployeeModel

class DepartmentListView(LoginRequiredMixin,ListView):
	login_url = reverse_lazy('login')
	model = models.DepartmentModel
	context_object_name = 'department_list'
	template_name = 'department_list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		sq = self.request.GET.get("search_query")
		search_type = self.request.GET.get("search_type")

		if sq is not None:
			if search_type == "name":
				qs = qs.filter(Q(name__icontains=sq))
		return qs

class DepartmentCreateView(LoginRequiredMixin,CreateView):
	login_url = reverse_lazy('login')
	model = models.DepartmentModel
	success_url = reverse_lazy("department_list")
	form_class = forms.DepartmentCreateForm
	template_name = 'department_create.html'

class DepartmentUpdateView(SuperuserRequiredMixin,LoginRequiredMixin,UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("department_list")
	model = models.DepartmentModel
	form_class = forms.DepartmentUpdateForm
	context_object_name = "department"
	template_name = 'department_update.html'

class DepartmentDeleteView(SuperuserRequiredMixin,LoginRequiredMixin,DeleteView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("department_list")
	model = models.DepartmentModel
	context_object_name = "department"
	template_name = 'department_delete.html'

class DepartmentDetailView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    context_object_name = 'employees'
    template_name = 'department_detail.html'

    def get_queryset(self): 
        queryset = EmployeeModel.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = models.DepartmentModel.objects.get(pk=self.kwargs['pk']) 
        return context