from django.urls import path
from expense import views

urlpatterns = [

	path('show_expense/', views.ExpenseListView.as_view(), name='expense_list'),
	path('new_expense/', views.ExpenseCreateView.as_view(), name='expense_create'),
	path('<int:pk>/edit/', views.ExpenseUpdateView.as_view(), name='expense_update'),
	path('<int:pk>/delete/', views.ExpenseDeleteView.as_view(), name='expense_delete'),
	path('<int:pk>', views.ExpenseDetailView.as_view(), name='expense_detail'),
]