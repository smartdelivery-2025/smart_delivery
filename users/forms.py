from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from companies.models import Company


class ClientRegisterForm(UserCreationForm):

    company_code = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['company_code', 'username', 'email', 'phone', 'password1', 'password2']

    def clean_company_code(self):
        code = self.cleaned_data.get('company_code')
        try:
            company = Company.objects.get(code=code)
        except Company.DoesNotExist:
            raise forms.ValidationError("Código de empresa inválido.")
        return code

    def save(self, commit=True):
        user = super().save(commit=False)
        company = Company.objects.get(code=self.cleaned_data['company_code'])
        user.company = company
        user.role = "CLIENTE"
        if commit:
            user.save()
        return user