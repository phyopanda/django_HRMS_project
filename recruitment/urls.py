from django.urls import path
from recruitment import views

urlpatterns = [

	path('show_recruitment/', views.RecruitmentListView.as_view(), name='recruitment_list'),
	path('new_recruitment/', views.RecruitmentCreateView.as_view(), name='recruitment_create'),
	path('<int:pk>/edit/', views.RecruitmentUpdateView.as_view(), name='recruitment_update'),
	path('<int:pk>/delete/', views.RecruitmentDeleteView.as_view(), name='recruitment_delete'),
	path('<int:pk>', views.RecruitmentDetailView.as_view(), name='recruitment_detail'),
]