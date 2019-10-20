from django import forms
class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=50, required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingresa tu nombre',
            }))
    email = forms.EmailField(label="Email", required=True,widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingresa tu email',
            }))
    content = forms.CharField(label="Contenido", max_length=50, required=True,widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Ingresa tu mensaje',
            'rows':5,
            }))