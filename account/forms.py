from django.forms import Form, CharField
from django.forms.utils import ErrorList


class RegistrationForm(Form):
    username = CharField(required=True)
    password = CharField(required=True)
    confirm_password = CharField(required=True)

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()

        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):
            self.errors['password'] = ErrorList('Passwords do not match')

        return cleaned_data
