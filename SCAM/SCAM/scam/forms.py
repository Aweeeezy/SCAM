from django.contrib.auth.forms import UserCreationForm
from django.utils.safestring import mark_safe
from SCAM.scam.models import Student
from django import forms


class CreateUserForm(UserCreationForm):

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.save()
        Student.objects.create(user=user, sid=user.username)
        return user


class ConnectForm(forms.Form):

    other_options = (('p', 'have taken'), ('c', 'are taking'), ('f', 'will take'))
    other_student = forms.ChoiceField(choices=other_options,
            widget=forms.Select(), required=True, label='')

    your_options= (('c', 'your current courses'), ('f', 'your future courses'))
    you = forms.ChoiceField(choices=your_options, widget=forms.Select(),
            required=True, label=mark_safe('<br/>'))
    you.label_suffix=''

