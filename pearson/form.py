from django.forms import ModelForm
from .models import Pearson


class PearsonForm(ModelForm):
    class Meta:
        model = Pearson
        fields = ['name', 'last_name', 'birth_date']
