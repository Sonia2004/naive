from django import forms

class EmailCheckForm(forms.Form):
    """Formulario para ingresar contenido de email."""
    subject = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Asunto del email (opcional)',
        })
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 8,
            'placeholder': 'Paste el contenido del email aquí...',
        }),
        help_text='Pegue el contenido completo del email'
    )
    raw_email = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 10,
            'placeholder': 'O pegue el email en formato raw aquí...',
        }),
        required=False,
        help_text='Alternativamente, pegue el email en formato raw (con headers)'
    )
