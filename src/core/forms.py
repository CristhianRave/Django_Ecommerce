from django import forms

class ContactForm(forms.Form):

    nombre = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(
            attrs={
        'placeholder': 'Tu nombre'
        }))

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
        'placeholder': 'Tu correo electronico'
        }))

    mensaje = forms.CharField(
        widget=forms.TextInput(
            attrs={
        'placeholder': 'Tu mensaje'
        }))