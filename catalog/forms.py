from django.contrib.auth.forms import UserCreationForm
from .models import Worker


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "position",
            "first_name",
            "last_name"
        )
