from django.shortcuts import render
from . import models, forms

# Create your views here.
def home(request):
    db_response = exists = is_allowed = None
    form = forms.ToDoListForm(request.POST or None)
    search_form = forms.SearchForm(data=request.GET or None)

    # ____________________________ ADD TASK _______________________________
    if request.method == 'POST' and form.is_valid() :
        data = form.cleaned_data

        # Check the task is existing on db or no
        db_response = models.ToDoList.objects.filter(name=data['name'])

        if len(db_response) != 0 :
            exists = True

        else:
            exists = False

        if data['name'].strip() == '':
            is_allowed = False

        else:
            is_allowed = True

        # add item on db
        if not exists and is_allowed:
            models.ToDoList.objects.create(name=data['name'])


    # _________________REMOVE TASK____________________________________
    if request.method == "GET":
        removed_name = request.GET.get('remove_value')
        db_result = models.ToDoList.objects.filter(name=removed_name)

        if len(db_result) == 1 :
            db_result.delete()

    # _____________________SEARCH TASK_______________________________________
    try:
        search_name = request.GET.get('name')

    except Exception as Error:
        print(Error)

    if search_name is not None:
        all_task = models.ToDoList.objects.filter(name__icontains=search_name)

    else:
        all_task = models.ToDoList.objects.all()


    return render(request, 'index.html', {'form_obj':form,
                                          'all_task':all_task, 'search_obj':search_form
                                          })

