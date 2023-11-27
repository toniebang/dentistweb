from django import forms
from .models import *
from django.forms import ModelForm, TextInput, EmailInput, Textarea

class CorreosForm(forms.ModelForm):
    class Meta:
        model = Correo
        fields = ('correos',)

        widgets = {
            'name': EmailInput(attrs={
                'placeholder':'Correo Electrónico', 'name':"nl-email"
            })
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['name', 'email', 'message']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control mb-30", 'placeholder':'Nombre'
            }),
            'email': EmailInput(attrs={
                'class': "form-control mb-30", 'placeholder':'Correo'
            }),
            'message': Textarea(attrs={
                'class': "form-control mb-30", 'placeholder':'Mensaje'
            })
        }
choices = (
        ("1", "Choose Your Time" ),
        ("2", "9 AM to 10 AM" ),
        ("3", "11 AM to 12 PM" ),
        ("4", "2 PM to 4 PM" ),
        ("5", "8 PM to 10 PM" ),
    )
class ApointmentForm(forms.ModelForm):
    
    class Meta:
        
        model = Cita
        fields = ['name', 'email', 'message', 'phone_number', 'schedule', 'address', 'asunto']
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control", 'placeholder':'Tu nombre y apellidos'
            }),
            'phone_number': TextInput(attrs={
                'class': "form-control", 'placeholder':'Tu numero de telefono'
            }),
            'address': TextInput(attrs={
                'class': "form-control", 'placeholder':'Tu Direccion'
            }),
            'email': EmailInput(attrs={
                'class': "form-control", 'placeholder':'Tu correo electronico'
            }),
            'message': Textarea(attrs={
                'class': "form-control", 'placeholder':'Tu mensaje'
            }),
            'schedule': TextInput(attrs={
                'class': "form-control", 'placeholder':'Fecha para la cita'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['asunto'].widget.attrs.update({
            'class': "form-control", 
        })
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields =  ['content']
        widgets = {


            'content': Textarea(attrs={
                'class': "form-control mb-30", 'placeholder':'Comentario'
            })
        }

            #         'name': TextInput(attrs={
            #     'class': "form-control mb-30", 'placeholder':'Nombre'
            # }),

            #             'email': EmailInput(attrs={
            #     'class': "form-control mb-30", 'placeholder':'Correo'
            # }),