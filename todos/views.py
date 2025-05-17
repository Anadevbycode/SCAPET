from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from .models import Todo
from django.urls import reverse_lazy

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):  # Corrigido "createView" para "CreateView"
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')

# Na TodoUpdateView (views.py)
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline']
    template_name = 'todos/todo_form.html'  # Caminho corrigido
    success_url = reverse_lazy('todo_list')

# Na TodoDeleteView (views.py)
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todos/todo_confirm_delete.html'  # Caminho corrigido
    success_url = reverse_lazy('todo_list')
    
class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished_at = date.today()
        todo.save()
        return redirect("todo_list")