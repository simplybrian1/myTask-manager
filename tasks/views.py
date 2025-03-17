from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required  # Ensure only logged-in users can create tasks
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  # Don't save yet
            task.user = request.user  # Assign the logged-in user
            task.save()  # Now save it
            return redirect("home")  # Redirect to task list
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm  # Assuming you have a form for tasks

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")  # Redirect to task list after saving
    else:
        form = TaskForm(instance=task)

    return render(request, "tasks/task_form.html", {"form": form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect("home")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect("home")  # ✅ Redirect to task list after deletion

    return render(request, "tasks/task_confirm_delete.html", {"task": task})
