from django import forms
from django.core.mail import send_mail
from django.forms import TextInput
from django.conf import settings

from email_sender_app.models import Email


class EmailAddForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']

        widgets = {
            'email': TextInput(attrs={
                'class': 'form-control',
                'aria-describedby': 'emailHelp',
                'placeholder': 'Enter email',
            }
            )
        }


class EmailSenderForm(forms.Form):
    name = forms.CharField(max_length=30)
    subject = forms.CharField(max_length=70)
    text = forms.CharField(widget=forms.Textarea)

    def construct_info(self):
        clean_data = super().clean()

        name = clean_data.get('name').strip()
        subject = clean_data.get('subject')
        text = clean_data.get('text')

        message = f'From {name}\n\n{text}'

        return subject, message

    def send(self):
        subject, message = self.construct_info()

        send_mail(subject=subject,
                  message=message,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[email_obj['email'] for email_obj in Email.objects.values()]
                  )
