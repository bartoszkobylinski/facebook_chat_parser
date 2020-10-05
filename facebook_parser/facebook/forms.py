from django.forms import forms


class FacebookChatForm(forms.Form):
    chat_file = forms.FileField()
