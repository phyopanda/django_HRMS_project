from department.models import DepartmentModel

def get_departments(request):

    department_list = DepartmentModel.objects.all().order_by('name')
    return { 'department_list':department_list}