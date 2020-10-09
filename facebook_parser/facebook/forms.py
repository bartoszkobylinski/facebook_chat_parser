from django.forms import forms
from django.contrib import messages
import json
from jsonschema import validate, ValidationError



class FacebookChatForm(forms.Form):
    chat_file = forms.FileField()

    def clean_chat_file(self):
        data = self.cleaned_data.get('chat_file')

        if data.content_type != "application/json":
            raise forms.ValidationError('Your file is not JSON file')
        return data
