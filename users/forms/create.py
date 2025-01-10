from django import forms
from users.models import Role, User

class CreateUser(forms.ModelForm):
    
    class Meta:
        model = User
        fields = "__all__"  # all User model fields
        widgets = {
            'role': forms.Select(attrs={'class': 'form-select'}),
        }
     
       
