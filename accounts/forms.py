# accounts/forms.py
from django import forms
from .models import User, Doctor

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']

class DoctorRegistrationForm(forms.ModelForm):
    user = UserRegistrationForm()
    certificate = forms.FileField()

    class Meta:
        model = Doctor
        fields = ['specialty', 'certificate']

    def save(self, commit=True):
        user_data = self.cleaned_data.pop('user')
        user = User.objects.create_user(**user_data)
        doctor = Doctor(user=user, **self.cleaned_data)
        if commit:
            doctor.save()
        return doctor
