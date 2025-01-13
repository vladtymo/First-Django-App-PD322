from django import forms
from users.models import User


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"  # all User model fields
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }
