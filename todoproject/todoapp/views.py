from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoListItem

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

# обработка запроса на публикацию
def addTodoView(request): 
    x = request.POST['content'] 
    new_item = TodoListItem(content = x) 
    new_item.save() 
    return HttpResponseRedirect('/todoapp/')