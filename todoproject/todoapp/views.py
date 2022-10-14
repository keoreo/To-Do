from django.shortcuts import render
from django.http import HttpResponseRedirect

def todoappView(request):
    return render(request, 'todolist.html')