from django.forms import ModelForm
from vacancy.models import Employee
from django.contrib.auth.models import User

# Create your forms here

class ApplyForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'