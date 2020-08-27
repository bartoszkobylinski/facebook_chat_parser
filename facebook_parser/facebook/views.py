import json
from django.shortcuts import render
from django.views.generic import FormView
from .forms import FacebookChatForm
from .models import FacebookChat, Participant
from .facebook_chat import FacebookChat1

# Create your views here.

'''
class UploadFileView(FormView):
    form_class = FacebookChatForm
    template_name = 'facebook_form.html'
    success_url = 'index'

    def form_valid(self, form):
        print('ttttt')
        print(form.file)
        return super().form_valid(form)

def correct_string_decoding(string):
        return string.encode('iso-8859-1').decode('utf-8)')

def get_chat_total_gifs_number(messages):
        gifs_counter = 0
        for gif in messages:
            print(f"that is {gif}")
            gif_length = len(gif.get('photos', ''))
            gifs_counter += gif_length
        return gifs_counter
'''


class UploadFileView(FormView):
    form_class = FacebookChatForm
    template_name = 'facebook_form.html'  # Replace with your template.
    success_url = 'index'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        file = request.FILES['file_chat']
        print(f'that is file {file}')

        if form.is_valid():
            file = json.load(file)
            # print(file.get('title',''))
            fb_chat = FacebookChat1()
            fb_chat.file = file
            # a.file = file
            fb_chat.messages
            
            print(f"that is participants number: {fb_chat.get_fb_chat_participants_number()}")
            print(f"that is massegs number: {fb_chat.get_fb_chat_total_messages_number()}")
            print(f"that is char number: {fb_chat.get_fb_chat_total_characters_number()}")
            print(f"that is photos number: {fb_chat.get_fb_chat_total_photos_number()}")
            print(f"that is links number: {fb_chat.get_fb_chat_total_links_number()}")
            print(f"that is gifs number: {fb_chat.get_fb_chat_total_gifs_number()}")
            print(f"that is reactions number: {fb_chat.get_fb_chat_reactions_number()}")
            fb_chat_model = FacebookChat(chat_title=fb_chat.get_fb_chat_title(),
                                     participants_number= fb_chat.get_fb_chat_participants_number(),
                                     gifs_number=fb_chat.get_fb_chat_total_gifs_number(),
                                     messages_number=fb_chat.get_fb_chat_total_messages_number(),
                                     photos_number=fb_chat.get_fb_chat_total_photos_number(),
                                     characters_number=fb_chat.get_fb_chat_total_characters_number(),
                                     reactions_number=fb_chat.get_fb_chat_reactions_number(),
                                     links_number=fb_chat.get_fb_chat_total_links_number()
                )
            fb_chat_model.save()
            '''
            print(f"that is title: {fb_chat.get_fb_chat_title()}")
            print(f"that are participants of chat: {fb_chat.get_fb_chat_participants()}")
            print(f"that is a word counter: {fb_chat.get_fb_chat_total_words_number()}")
            # print(f"that is a chat word frequency: {fb_chat.find_chat_word_frequency('bartek')}")
            print(f"that are participants: {fb_chat.get_fb_chat_participants()}")
            fb_chat_b = FacebookChat(chat_title=fb_chat.get_fb_chat_title(),
                                     gifs_number=fb_chat.get_fb_chat_total_gifs_number(),
                                     photos_number=fb_chat.get_fb_chat_total_photos_number(),
                                     characters_number=fb_chat.get_fb_chat_total_characters_number(),
                                     message_number=fb_chat.get_fb_chat_total_messages_number()
                                     )
            print(fb_chat_b)
            fb_chat_b.save()
            for f in files:
                file = json.load(f)
                mess_title = file['title']
                fb_chat = FacebookChat(chat_title=mess_title)
                fb_chat.save()
                # print(f"I have saved a fb_chat {fb_chat}")
                for participant in file['participants']:
                    partic = participant.get('name', '')
                    partic = Participant(name=partic, facebook_chat=fb_chat)
                    # print(f"that is partic: {partic}")
                    partic.save()
                a = f.read()
            '''
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
