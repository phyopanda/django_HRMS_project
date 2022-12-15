from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from contract import models
from contract import forms

from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.db.models import Q

class ContractListView(LoginRequiredMixin,ListView):
	login_url = reverse_lazy('login')
	model = models.ContractModel
	context_object_name = 'contract_list'
	template_name = 'contract_list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		sq = self.request.GET.get("search_query")
		search_type = self.request.GET.get("search_type")

		if sq is not None:
			if search_type == "name":
				qs = qs.filter(Q(name__icontains=sq))
		return qs

class ContractCreateView(LoginRequiredMixin,CreateView):
	login_url = reverse_lazy('login')
	model = models.ContractModel
	success_url = reverse_lazy("contract_list")
	form_class = forms.ContractCreateForm
	template_name = 'contract_create.html'

class ContractUpdateView(LoginRequiredMixin,UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("contract_list")
	model = models.ContractModel
	form_class = forms.ContractUpdateForm
	context_object_name = "contract"
	template_name = 'contract_update.html'

class ContractDeleteView(LoginRequiredMixin,DeleteView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("contract_list")
	model = models.ContractModel
	context_object_name = "contract"
	template_name = 'contract_delete.html'

class ContractDetailView(LoginRequiredMixin,DetailView):
	login_url = reverse_lazy('login')
	model = models.ContractModel
	context_object_name = "contract"
	template_name = 'contract_detail.html'