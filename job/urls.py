from django.urls import path
from job import views

urlpatterns = [

	path('show_job/', views.JobListView.as_view(), name='job_list'),
	path('new_job/', views.JobCreateView.as_view(), name='job_create'),
	path('<int:pk>/edit/', views.JobUpdateView.as_view(), name='job_update'),
	path('<int:pk>/delete/', views.JobDeleteView.as_view(), name='job_delete'),
	path('<int:pk>', views.JobDetailView.as_view(), name='job_detail'),
]