from django.forms import forms


class FacebookChatForm(forms.Form):
    chat_file = forms.FileField()

    def clean_chat_file(self):
        data = self.cleaned_data.get("chat_file")

        if data.content_type == "application/json":
            return data
        else:
            raise forms.ValidationError(
                "Your file is not JSON file. Let's try with another one."
            )
