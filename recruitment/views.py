from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from recruitment import models
from recruitment import forms

from django.urls import reverse_lazy
from braces.views import SuperuserRequiredMixin, LoginRequiredMixin
from django.db.models import Q

class RecruitmentListView(LoginRequiredMixin,ListView):
	login_url = reverse_lazy('login')
	model = models.RecruitmentModel
	context_object_name = 'recruitment_list'
	template_name = 'recruitment_list.html'

	def get_queryset(self):
		qs = super().get_queryset()
		sq = self.request.GET.get("search_query")
		search_type = self.request.GET.get("search_type")

		if sq is not None:
			if search_type == "name":
				qs = qs.filter(Q(name__icontains=sq))
		return qs

class RecruitmentCreateView(CreateView):
	
	model = models.RecruitmentModel
	success_url = reverse_lazy("cvform")
	form_class = forms.RecruitmentCreateForm
	template_name = 'cv_form.html'

class RecruitmentUpdateView(SuperuserRequiredMixin,LoginRequiredMixin,UpdateView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("recruitment_list")
	model = models.RecruitmentModel
	form_class = forms.RecruitmentUpdateForm
	context_object_name = "recruitment"
	template_name = 'recruitment_update.html'

class RecruitmentDeleteView(SuperuserRequiredMixin,LoginRequiredMixin,DeleteView):
	login_url = reverse_lazy('login')
	success_url = reverse_lazy("recruitment_list")
	model = models.RecruitmentModel
	context_object_name = "recruitment"
	template_name = 'recruitment_delete.html'

class RecruitmentDetailView(LoginRequiredMixin,DetailView):
	login_url = reverse_lazy('login')
	model = models.RecruitmentModel
	context_object_name = "recruitment"
	template_name = 'recruitment_detail.html'