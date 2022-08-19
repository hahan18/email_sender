# email_sender BY ALEXANDR KHAKHANOVSKYI
There is a send mail app with GUI based on Django using Django's send_mail function.
Absolute goal of this app is to provide mass mail sender with minimal interaction with the code.


# HOW TO INSTALL (FOR WINDOWS)
git clone https://github.com/hahan18/email_sender.git

Into email_sender path use: python -m venv venv,
Then use: venv\Scripts\activate.


Run pip install -r requirements.txt


Into email_sender/email_sender_proj/email_sender_proj path create .env file with fields

EMAIL_HOST= # Custom tag for change email host (for gmail - smtp.gmail.com)
EMAIL_HOST_USER=  # Your email
EMAIL_HOST_PASSWORD=  # Special application password


Run python manage.py makemigrations
Then run python manage.py migrate

Run python manage.py runserver and enjoy the app!
