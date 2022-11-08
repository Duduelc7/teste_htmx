from django import forms
from .models import Empresas


class EmpresasForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Empresas
        fields = ('empresa', 'cnpj')
        widgets = {
            'empresa': forms.TextInput(attrs={'placeholder': 'Empresa', 'autofocus': True}),
            'cnpj': forms.NumberInput(attrs={'placeholder': 'cnpj'}),
        }        


    def __init__(self, *args, **kwargs):
        super(EmpresasForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        fields = ["name", "phone_number"]
        model = Contact
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
        }

class RegiaoForm(forms.ModelForm):
    class Meta:
        fields = ["regiao"]

    widgets = {
        "regiao": forms.TextInput(attrs={"class": "form-control"})
    }