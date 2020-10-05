import json
from django.contrib import messages
from django.views.generic import FormView, TemplateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .forms import FacebookChatForm
from .models import FacebookChat as FacebookChatModel
from .models import Participant as ParticipantModel
from .models import Word as WordModel
from .facebook_chat import FacebookChat
from .participant import Participant
from django.http import request

class UploadFileView(FormView):
    form_class = FacebookChatForm
    template_name = 'facebook_form.html'
    success_url = 'index'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        file = request.FILES['chat_file']
        if form.is_valid():
            file = json.load(file)
            fb_chat = FacebookChat()
            fb_chat.file = file
            fb_chat.messages
            #fb_chat.fb_chat_correct_messages_decoding()
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
                #print(participant)
                partic = Participant(participant, fb_chat.file)
                reaction_stat = partic.get_participant_reactions_number()
                if reaction_stat[0] > 0:
                    participant_reaction_number = reaction_stat[0]
                    participant_most_common_react = reaction_stat[1][0][0]
                    participant_counter_most_common_react = reaction_stat[1][0][1]
                else:
                    participant_reaction_number = 0
                    participant_most_common_react = '-'
                    participant_counter_most_common_react = 0
                participant_model = ParticipantModel(gifs_number=partic.get_participant_gifs_number(),
                                                  messages_number=partic.get_participants_messages_number(),
                                                  photos_number=partic.get_participant_photos_number(),
                                                  characters_number=partic.get_participant_characters_number(),
                                                  words_number=partic.get_participant_words_number(),
                                                  links_number=partic.get_participant_links_number(),
                                                  total_numbers_of_reactions=participant_reaction_number,
                                                  counter_most_common_react=participant_counter_most_common_react,
                                                  most_common_reaction=participant_most_common_react,
                                                  name=participant,
                                                  facebook_chat=fb_chat_model
                    )
                #print(participant_model.counter_most_common_react)
                participant_model.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
class ChartView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        messages_list = []
        characters_list = []
        photos_list = []
        links_list = []
        gifs_list = []
        users_list = []
        words_list = []
        reaction_list = []
        numbers_react_list = []
        title = FacebookChatModel.objects.all()
        title = title[0].chat_title
        print(title)
        for user in ParticipantModel.objects.all():
            users_list.append(user.name)
            messages_number = ParticipantModel.objects.filter(name=user.name).values('messages_number')
            for message_number in messages_number:
                messages_list.append(message_number.get('messages_number',''))
            words_number = ParticipantModel.objects.filter(name=user.name).values('words_number')
            for word_number in words_number:
                words_list.append(word_number.get('words_number',''))

            characters_number = ParticipantModel.objects.filter(name=user.name).values('characters_number')
            for character_number in characters_number:
                characters_list.append(character_number.get('characters_number',''))
            
            photos_number = ParticipantModel.objects.filter(name=user.name).values('photos_number')
            for photo_number in photos_number:
                photos_list.append(photo_number.get('photos_number',''))
            
            links_number = ParticipantModel.objects.filter(name=user.name).values('links_number')
            for link_number in links_number:
                links_list.append(link_number.get('links_number',''))
            
            gifs_number = ParticipantModel.objects.filter(name=user.name).values('gifs_number')
            for gif_number in gifs_number:
                gifs_list.append(gif_number.get('gifs_number'))
            
            reactions = ParticipantModel.objects.filter(name=user.name).values('most_common_reaction')
            #print(f'that is after query set: {reaction} and {user.name}')
            for react in reactions:
                reaction_list.append(react.get('most_common_reaction'))
            number_of_reactions = ParticipantModel.objects.filter(name=user.name).values("counter_most_common_react")
            for number in number_of_reactions:
                numbers_react_list.append(number.get('counter_most_common_react'))

        context.update(title=title)
        context.update(reaction_list=zip(users_list, reaction_list, numbers_react_list))
        context.update(links_list=links_list)
        context.update(words_list=words_list)
        context.update(users_list=users_list)
        context.update(messages_list=messages_list)
        context.update(characters_list=characters_list)
        context.update(gifs_list=gifs_list)
        context.update(photos_list=photos_list)
        return context


class DeleteFaceView(TemplateView):
    template_name = 'delete.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        queryset = FacebookChatModel.objects.all()
        queryset.delete()
        return context

'''
class DeleteFaceView(DeleteView):
    model = FacebookChatModel
    success_url = 'facebook'

    def get_object(self):

        id_ = self.kwargs.get("id")
        return get_object_or_404(FacebookChatModel, id=id_)

    def get_queryset(self):
        self.queryset = FacebookChatModel.objects.get(pk=id)
        self.queryset.delete()
        messages.add_message(self.request, messages.INFO, 'Your file was succsesfully deleted!')
'''