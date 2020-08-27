from django.forms import forms


class FacebookChatForm(forms.Form):
    file_chat = forms.FileField()
