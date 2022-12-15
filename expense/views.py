from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from expense import models
from expense import forms

from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.db.models import Q

class ExpenseListView(LoginRequiredMixin,ListView):
	login_url = reverse_lazy('login')
	model = models.ExpenseModel
	context_object_name = 'expense_list'
	template_name = 'expense_list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		sq = self.request.GET.get("search_query")
		search_type = self.request.GET.get("search_type")

		if sq is not None:
			if search_type == "name":
				qs = qs.filter(Q(name__icontains=sq))
		return qs

class ExpenseCreateView(LoginRequiredMixin,CreateView):
	login_url = reverse_lazy('login')
	model = models.ExpenseModel
	success_url = reverse_lazy("expense_list")
	form_class = forms.ExpenseCreateForm
	template_name = 'expense_create.html'

class ExpenseUpdateView(SuperuserRequiredMixin,LoginRequiredMixin,UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("expense_list")
	model = models.ExpenseModel
	form_class = forms.ExpenseUpdateForm
	context_object_name = "expense"
	template_name = 'expense_update.html'

class ExpenseDeleteView(SuperuserRequiredMixin,LoginRequiredMixin,DeleteView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("expense_list")
	model = models.ExpenseModel
	context_object_name = "expense"
	template_name = 'expense_delete.html'

class ExpenseDetailView(LoginRequiredMixin,DetailView):
	login_url = reverse_lazy('login')
	model = models.ExpenseModel
	context_object_name = "expense"
	template_name = 'expense_detail.html'