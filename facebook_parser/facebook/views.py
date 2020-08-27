import json
from django.views.generic import FormView
from .forms import FacebookChatForm
from .models import FacebookChat as FacebookChatModel
from .models import Participant as ParticipantModel
from .facebook_chat import FacebookChat
from .participant import Participant


class UploadFileView(FormView):
    form_class = FacebookChatForm
    template_name = 'facebook_form.html'  # Replace with your template.
    success_url = 'index'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        file = request.FILES['file_chat']
        if form.is_valid():
            file = json.load(file)
            fb_chat = FacebookChat()
            fb_chat.file = file
            fb_chat.messages
            fb_chat_model = FacebookChatModel(chat_title=fb_chat.get_fb_chat_title(),
                                     participants_number= fb_chat.get_fb_chat_participants_number(),
                                     gifs_number=fb_chat.get_fb_chat_total_gifs_number(),
                                     messages_number=fb_chat.get_fb_chat_total_messages_number(),
                                     photos_number=fb_chat.get_fb_chat_total_photos_number(),
                                     characters_number=fb_chat.get_fb_chat_total_characters_number(),
                                     reactions_number=fb_chat.get_fb_chat_reactions_number(),
                                     links_number=fb_chat.get_fb_chat_total_links_number()
                )
            fb_chat_model.save()
            for participant in fb_chat.get_fb_chat_participants():
                partic = Participant(participant, fb_chat.file)
                participant_model = ParticipantModel(gifs_number=partic.get_participant_gifs_number(),
                                                  messages_number=partic.get_participants_messages_number(),
                                                  photos_number=partic.get_participant_photos_number(),
                                                  characters_number=partic.get_participant_characters_number(),
                                                  links_number=partic.get_participant_links_number(),
                                                  name=participant,
                                                  facebook_chat=fb_chat_model
                    )
                participant_model.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
