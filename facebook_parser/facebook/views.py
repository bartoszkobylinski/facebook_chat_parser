import json
from collections import Counter
from django.contrib import messages
from django.views.generic import FormView, TemplateView
from facebook.forms import FacebookChatForm
from facebook.models import FacebookChat as FacebookChatModel
from facebook.models import Participant as ParticipantModel
from facebook.models import (FourCharWord, FiveCharWord, SixCharWord, 
                             SevenCharWord, EightCharWord, NineCharWord,
                             TenAndMoreCharWord)
from facebook.facebook_chat import FacebookChat
from facebook.participant import Participant



class UploadFileView(FormView):
    form_class = FacebookChatForm
    template_name = 'facebook_form.html'
    success_url = 'index'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            file = request.FILES['chat_file']
            try:
                file = json.load(file)
            except UnicodeDecodeError:
                messages.error(self.request, "that is error")
            fb_chat = FacebookChat()
            fb_chat.file = file
            fb_chat.messages
            words_dict = fb_chat.creating_dict_with_words_occurance_sorted_by_length()
            print(words_dict.keys())
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
                reaction_stat = partic.get_participant_reactions_number()
                if reaction_stat[0] > 0:
                    participant_reaction_number = reaction_stat[0]
                    participant_most_common_react = reaction_stat[1][0][0]
                    participant_counter_most_common_react = reaction_stat[1][0][1]
                else:
                    participant_reaction_number = 0
                    participant_most_common_react = '-'
                    participant_counter_most_common_react = 0
                participant_model = ParticipantModel(
                    gifs_number=partic.get_participant_gifs_number(),
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
                participant_model.save()
                
                for key, value in words_dict.get(participant, '').items():
                    for word in Counter(value).most_common(3):
                        if key == 'four':
                            this_word = FourCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
                        elif key == 'five':
                            this_word = FiveCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
                        elif key == 'six':
                            this_word = SixCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
                        elif key == 'seven':
                            this_word = SevenCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
                        elif key =='eight':
                            this_word = EightCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
                        elif key == 'nine':
                            this_word = NineCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
                        elif key == 'ten':
                            this_word = TenAndMoreCharWord(participant=participant_model, count=word[1], word=[0])
                            this_word.save()
                            
                        
                            
                    
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
        four_char_word_list = []
        five_char_word_list = []
        six_char_word_list = []
        seven_char_word_list = []
        eight_char_word_list = []
        nine_char_word_list = []
        ten_char_word_list = []
        title = FacebookChatModel.objects.all()
        title = title[0].chat_title
        for user in ParticipantModel.objects.all():
            users_list.append(user.name)
            participant_fb = ParticipantModel.objects.filter(name=user.name).last()
            messages_list.append(participant_fb.messages_number)
            words_list.append(participant_fb.words_number)
            characters_list.append(participant_fb.characters_number)
            photos_list.append(participant_fb.photos_number)
            links_list.append(participant_fb.links_number)
            gifs_list.append(participant_fb.gifs_number)
            reactions_queryset = ParticipantModel.objects.filter(name=user.name).values('most_common_reaction')
            reaction_list.append(reactions_queryset[0].get('most_common_reaction'))
            number_of_reactions_queryset = ParticipantModel.objects.filter(name=user.name).values("counter_most_common_react")
            numbers_react_list.append(number_of_reactions_queryset[0].get('counter_most_common_react'))
            four_char_words = list(FourCharWord.objects.filter(participant=user).values("count", "word"))
            five_char_words = list(FiveCharWord.objects.filter(participant=user).values("count", "word"))
            six_char_words = list(SixCharWord.objects.filter(participant=user).values("count", "word"))
            seven_char_words = list(SevenCharWord.objects.filter(participant=user).values("count", "word"))
            eight_char_words = list(EightCharWord.objects.filter(participant=user).values("count", "word"))
            nine_char_words = list(NineCharWord.objects.filter(participant=user).values("count", "word"))
            ten_char_words = list(TenAndMoreCharWord.objects.filter(participant=user).values("count", "word"))
            four_char_word_list.append(four_char_words)
            five_char_word_list.append(five_char_words)
            six_char_word_list.append(six_char_words)
            seven_char_word_list.append(seven_char_words)
            eight_char_word_list.append(eight_char_words)
            nine_char_word_list.append(nine_char_words)
            ten_char_word_list.append(ten_char_words)
        context.update(title=title)
        context.update(reaction_list=sorted(zip(users_list, reaction_list, numbers_react_list), key=lambda x:x[2], reverse=True))
        context.update(links_list=links_list)
        context.update(words_list=words_list)
        context.update(users_list=users_list)
        context.update(messages_list=messages_list)
        context.update(characters_list=characters_list)
        context.update(gifs_list=gifs_list)
        context.update(photos_list=photos_list)
        context.update(user_messages_list=sorted(zip(users_list, messages_list), key=lambda x:x[1], reverse=True))
        context.update(user_characters_list=sorted(zip(users_list, characters_list), key=lambda x:x[1], reverse=True))
        context.update(user_words_list=sorted(zip(users_list, words_list),key=lambda x:x[1], reverse=True))
        context.update(user_photos_list=sorted(zip(users_list, photos_list), key=lambda x:x[1], reverse=True))
        context.update(user_links_list=sorted(zip(users_list, links_list), key=lambda x:x[1], reverse=True))
        context.update(user_gifs_list=sorted(zip(users_list, gifs_list), key=lambda x:x[1], reverse=True))
        context.update(four_char_words=list(zip(users_list, four_char_word_list)))
        context.update(five_char_words=list(zip(users_list, five_char_word_list)))
        context.update(six_char_words=list(zip(users_list, six_char_word_list)))
        context.update(seven_char_words=list(zip(users_list, seven_char_word_list)))
        context.update(eight_char_words=list(zip(users_list, eight_char_word_list)))
        context.update(nine_char_words=list(zip(users_list, nine_char_word_list)))
        context.update(ten_char_words=list(zip(users_list, ten_char_word_list)))
        print(context['ten_char_words'])
        return context


class DeleteFaceView(TemplateView):
    template_name = 'delete.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        queryset = FacebookChatModel.objects.all()
        queryset.delete()
        return context
