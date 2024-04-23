from django.forms import ModelForm
from app.models import TODO


class todoform(ModelForm):
    class Meta:
        model= TODO
        fields=['title','status','priority']

