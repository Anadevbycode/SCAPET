from django.views.generic import ListView, CreateView, UpdateView, DeleteView  # Corrigido "vlews" para "views"
from django.urls import reverse_lazy
from .models import Todo  # Certifique-se de ter esse modelo criado

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