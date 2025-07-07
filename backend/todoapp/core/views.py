from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

def index(request):
    items = Todo.objects.order_by("-date")
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()  # Ahora guarda directamente el timezone seleccionado
            messages.success(request, "¡Tarea añadida correctamente!")
            return redirect('core:index')
    else:
        # Si el usuario está autenticado, usa su timezone preferido
        initial = {}
        if hasattr(request, 'user') and request.user.is_authenticated:
            initial['timezone'] = getattr(request.user, 'timezone', 'America/Caracas')
        form = TodoForm(initial=initial)

    context = {
        "forms": form,
        "list": items,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', context)

def remove(request, item_id):
    try:
        item = Todo.objects.get(id=item_id)
        item.delete()
        messages.success(request, "¡Tarea eliminada correctamente!")
    except Todo.DoesNotExist:
        messages.error(request, "La tarea no existe")
    
    return redirect('core:index')