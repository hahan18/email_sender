from django.urls import path

from .views import MainPage, EmailsListPage, EmailsSender, EmailsAddPage, email_delete, SuccessSendEmail

app_name = 'emails'

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('emails_list', EmailsListPage.as_view(), name='emails_list'),
    path('add', EmailsAddPage.as_view(), name='emails_add'),
    path('delete/<pk>', email_delete, name='emails_delete'),
    path('emails_sender', EmailsSender.as_view(), name='emails_sender'),
    path('success_send_email', SuccessSendEmail.as_view(), name='success_send_email')
]
