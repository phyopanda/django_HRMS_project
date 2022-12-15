from django.urls import path
from department import views

urlpatterns = [

	path('show_department/', views.DepartmentListView.as_view(), name='department_list'),
	path('new_department/', views.DepartmentCreateView.as_view(), name='department_create'),
	path('<int:pk>/edit/', views.DepartmentUpdateView.as_view(), name='department_update'),
	path('<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),
	path('<int:pk>', views.DepartmentDetailView.as_view(), name='department_detail'),
]