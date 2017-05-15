from django.contrib.auth.forms import UserCreationForm
from SCAM.scam.models import Student


class CreateUserForm(UserCreationForm):

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.save()
        Student.objects.create(user=user, sid=user.username)
        return user
