from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        widgets = {
            # Setting bootstrap classes and placeholders to model fields
            'team_name': forms.TextInput(attrs={'class': 'form-control input-md', 'placeholder': 'Lagnavn'}),
            'team_from': forms.TextInput(attrs={'class': 'form-control input-md', 'placeholder': 'Lag/sted'}),
            'tournament_class': forms.Select(attrs={'class': 'form-control input-md'}),
            'email': forms.TextInput(attrs={'class': 'form-control input-md', 'placeholder': 'eksempel@eksempel.no'}),
            'phone': forms.TextInput(attrs={'class': 'form-control input-md', 'placeholder': '12345678'}),
            'other': forms.Textarea(attrs={'class': 'form-control input-md', 'placeholder': 'Annen informasjon'})

        }
        fields = '__all__'
