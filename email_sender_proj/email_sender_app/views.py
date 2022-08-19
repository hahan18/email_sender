from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, FormView

from .forms import EmailSenderForm, EmailAddForm
from .models import Email


class MainPage(TemplateView):
    template_name = 'main_page.html'


class EmailsListPage(TemplateView):
    template_name = 'emails_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emails'] = Email.objects.all()
        return context


class EmailsAddPage(FormView):
    template_name = 'emails_add.html'
    form_class = EmailAddForm
    success_url = 'emails_list'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        Email.objects.create(email=email)
        return super().form_valid(form)


class EmailsSender(FormView):
    template_name = 'email_sender.html'
    form_class = EmailSenderForm
    success_url = 'success_send_email'

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)


class SuccessSendEmail(TemplateView):
    template_name = 'success_send_email.html'


def email_delete(request, pk):
    email = get_object_or_404(Email, pk=pk)
    if request.method == 'POST':
        email.delete()
        return redirect('emails:emails_list')

