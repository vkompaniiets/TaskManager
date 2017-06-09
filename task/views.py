from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse

from task.forms import add_task_form, edit_task_form
from task.models import Task


@login_required
def show_all_tasks(request):
    data = Task.objects.all()

    return TemplateResponse(request, 'all_tasks.html', {
        'tasks': data
    })


@login_required
def add(request):
    if request.method == 'POST':
        form = add_task_form(request.POST)
        if form.is_valid():
            Task(
                assignee=form.cleaned_data.get('assignee'),
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                created_by=request.user
            ).save()
            return HttpResponseRedirect(reverse('show_all_tasks'))
        else:
            return TemplateResponse(request, 'edit_task.html', {'errors': form.errors})
    else:
        return TemplateResponse(request, 'edit_task.html', {})


@login_required
def mark_done(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        task.completed = True
        task.save(update_fields=['completed'])
    except Task.DoesNotExist:
        raise Http404

    return HttpResponseRedirect(reverse('show_all_tasks'))


@login_required
def edit(request, task_id):
    if request.method == 'POST':
        form = edit_task_form(instance=Task.objects.get(id=task_id), data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('show_all_tasks'))
        return TemplateResponse(request, 'edit_task.html', {'errors': form.errors})
    else:
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise Http404

        form = edit_task_form(instance=task)
        return TemplateResponse(request, 'edit_task.html', {'form': form, 'edit': True, 'task_id': task_id})


@login_required
def delete(request, task_id):
    try:
        Task.objects.get(id=task_id).delete()
    except Task.DoesNotExist:
        raise Http404

    return HttpResponseRedirect(reverse('show_all_tasks'))
