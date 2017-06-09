from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, Form

from task.models import Task


class add_task_form(Form):
    name = CharField(required=True)
    assignee = CharField(required=False)
    description = CharField(required=False)

    def clean_assignee(self):
        assignee = self.cleaned_data.get('assignee')
        try:
            return User.objects.get(username=assignee)
        except User.DoesNotExist:
            raise ValidationError('Assignee does not exist')


class edit_task_form(ModelForm):
    class Meta:
        model = Task
        fields = ['assignee', 'name', 'description', 'completed']