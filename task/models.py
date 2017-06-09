from django.contrib.auth.models import User
from django.db.models import Model, DateTimeField, ForeignKey, CharField, BooleanField


class Task(Model):
    assignee = ForeignKey(User, blank=True, null=True, related_name='assignee')
    created_by = ForeignKey(User)
    name = CharField(max_length=50)
    completed = BooleanField(default=False)
    description = CharField(max_length=1000, blank=True, null=True)
    created = DateTimeField(auto_now_add=True)
    modified = DateTimeField(auto_now=True)
