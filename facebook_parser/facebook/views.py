import json
import time
from itertools import cycle
from collections import Counter
from django.views.generic import FormView, TemplateView
from facebook.forms import FacebookChatForm
from facebook.models import FacebookChat as FacebookChatModel
from facebook.models import Participant as ParticipantModel
from facebook.models import (
    FourCharWord,
    FiveCharWord,
    SixCharWord,
    SevenCharWord,
    EightCharWord,
    NineCharWord,
    TenAndMoreCharWord,
)

from facebook.facebook_classes import FacebookChat
from facebook.facebook_classes import Participant


class UploadFileView(FormView):
    form_class = FacebookChatForm
    template_name = "facebook_form.html"
    success_url = "index"

    def post(self, request, *args, **kwargs):
        start = time.time()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            files = request.FILES.getlist("chat_file")
            facebook_messages = []
            participants = []
            word_length = []
            chat_title = None
            words_dict = {}
            for file in files:
                file = json.load(file)
                temp_facebook_chat = FacebookChat(file)
                temp_facebook_chat.correct_messages_decoding()
                facebook_messages.extend(temp_facebook_chat.messages)
                participants.extend(temp_facebook_chat.participants)
                if chat_title is None:
                    chat_title = temp_facebook_chat.correct_string_decoding(temp_facebook_chat.file.get('title'))
                word_length.extend(temp_facebook_chat.LENGTH_OF_WORDS)
                temp_words_dict = temp_facebook_chat.creating_dict_with_words_occurance_sorted_by_length()
                words_dict.update(temp_words_dict)
            facebook_chat_model = FacebookChatModel(chat_title=chat_title)
            facebook_chat_model.save()
            participants = list(set(participants))
            for participant in participants:
                participant_messages = [
                    message for message in facebook_messages if message.get("sender_name") == participant]
                facebook_participant = Participant(participant, participant_messages)
                reaction_stat = facebook_participant.get_participant_reactions_number(facebook_messages)
                if reaction_stat[0] > 0:
                    participant_reaction_number = reaction_stat[0]
                    participant_most_common_react = reaction_stat[1][0][0]
                    participant_counter_most_common_react = reaction_stat[1][0][1]
                else:
                    participant_reaction_number = 0
                    participant_most_common_react = "-"
                    participant_counter_most_common_react = 0
                participant_model = ParticipantModel(
                    name=participant,
                    messages_number=facebook_participant.get_participant_messages_number(),
                    gifs_number=facebook_participant.get_participant_gifs_number(),
                    photos_number=facebook_participant.get_participant_photos_number(),
                    characters_number=facebook_participant.get_participant_characters_number(),
                    words_number=facebook_participant.get_participant_words_number(),
                    links_number=facebook_participant.get_participant_links_number(),
                    total_numbers_of_reactions=participant_reaction_number,
                    counter_most_common_react=participant_counter_most_common_react,
                    most_common_reaction=participant_most_common_react,
                    facebook_chat=facebook_chat_model,
                    )
                participant_model.save()
                for key, value in words_dict.get(participant, "").items():
                    occurrence = 3
                    for word in Counter(value).most_common(occurrence):
                        if key == "four":
                            this_word = FourCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
                        elif key == "five":
                            this_word = FiveCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
                        elif key == "six":
                            this_word = SixCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()

                        elif key == "seven":
                            this_word = SevenCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
                        elif key == "eight":
                            this_word = EightCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
                        elif key == "nine":
                            this_word = NineCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
                        elif key == "ten":
                            this_word = TenAndMoreCharWord(participant=participant_model, count=word[1], word=word[0])
                            this_word.save()
            end = time.time()
            print(f"that is time: {end - start} s")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ChartView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        word = request.GET.get("word")
        if word:
            if len(word) == 4:
                context["word"] = FourCharWord.objects.filter(word=word).order_by("-count")
            elif len(word) == 5:
                context["word"] = FiveCharWord.objects.filter(word=word).order_by("-count")
            elif len(word) == 6:
                context["word"] = SixCharWord.objects.filter(word=word).order_by("-count")
            elif len(word) == 7:
                context["word"] = SevenCharWord.objects.filter(word=word).order_by("-count")
            elif len(word) == 8:
                context["word"] = EightCharWord.objects.filter(word=word).order_by("-count")
            elif len(word) == 9:
                context["word"] = NineCharWord.objects.filter(word=word).order_by("-count")
            elif len(word) == 10:
                context["word"] = TenAndMoreCharWord.objects.filter(word=word).order_by("-count")
        return self.render_to_response(context)

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
        facebook_chat = FacebookChatModel.objects.latest("id")
        for user in ParticipantModel.objects.select_related("facebook_chat").filter(
                facebook_chat__chat_title=facebook_chat.chat_title):
            users_list.append(user.name)
            participant_fb = ParticipantModel.objects.filter(name=user.name).last()
            messages_list.append(participant_fb.messages_number)
            words_list.append(participant_fb.words_number)
            characters_list.append(participant_fb.characters_number)
            photos_list.append(participant_fb.photos_number)
            links_list.append(participant_fb.links_number)
            gifs_list.append(participant_fb.gifs_number)
            reactions_queryset = ParticipantModel.objects.filter(name=user.name).values("most_common_reaction")
            reaction_list.append(reactions_queryset[0].get("most_common_reaction"))
            number_of_reactions_queryset = ParticipantModel.objects.filter(name=user.name).values(
                "counter_most_common_react")
            numbers_react_list.append(number_of_reactions_queryset[0].get("counter_most_common_react"))
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
        charts_colors_list = self.create_color_list_for_chart(users_list)
        charts_border_colors_list = self.create_color_border_list_for_chat(charts_colors_list)
        context.update(title=facebook_chat.chat_title)
        context.update(reaction_list=sorted(zip(users_list, reaction_list, numbers_react_list), key=lambda x: x[2],
                                            reverse=True))
        context.update(links_list=links_list)
        context.update(words_list=words_list)
        context.update(users_list=users_list)
        context.update(messages_list=messages_list)
        context.update(characters_list=characters_list)
        context.update(gifs_list=gifs_list)
        context.update(photos_list=photos_list)
        context.update(user_messages_list=sorted(zip(users_list, messages_list), key=lambda x: x[1], reverse=True))
        context.update(user_characters_list=sorted(zip(users_list, characters_list), key=lambda x: x[1], reverse=True))
        context.update(user_words_list=sorted(zip(users_list, words_list), key=lambda x: x[1], reverse=True))
        context.update(user_photos_list=sorted(zip(users_list, photos_list), key=lambda x: x[1], reverse=True))
        context.update(user_links_list=sorted(zip(users_list, links_list), key=lambda x: x[1], reverse=True))
        context.update(user_gifs_list=sorted(zip(users_list, gifs_list), key=lambda x: x[1], reverse=True))
        context.update(four_char_words=list(zip(users_list, four_char_word_list)))
        context.update(five_char_words=list(zip(users_list, five_char_word_list)))
        context.update(six_char_words=list(zip(users_list, six_char_word_list)))
        context.update(seven_char_words=list(zip(users_list, seven_char_word_list)))
        context.update(eight_char_words=list(zip(users_list, eight_char_word_list)))
        context.update(nine_char_words=list(zip(users_list, nine_char_word_list)))
        context.update(ten_char_words=list(zip(users_list, ten_char_word_list)))
        context.update(
            message_statistic=sorted(
                zip(users_list, messages_list, words_list, characters_list), key=lambda x: x[1], reverse=True))
        context.update(charts_colors_list=charts_colors_list)
        context.update(borders_color_list=charts_border_colors_list)
        return context

    def create_color_list_for_chart(self, user_list):

        colors_list = ['rgba(255, 99, 132, 0.6)',
                       'rgba(54, 162, 235, 0.6)',
                       'rgba(255, 206, 86, 0.6)',
                       'rgba(75, 192, 192, 0.6)',
                       'rgba(153, 102, 255, 0.6)',
                       'rgba(255, 159, 64, 0.6)',
                       'rgba(75, 192, 192, 0.6)',
                       'rgba(153, 102, 255, 0.6)',
                       'rgba(255, 159, 64, 0.6)'
                       ]
        colors = cycle(colors_list)
        chart_colors_list = [
            next(colors) for user in range(len(user_list))
        ]
        return chart_colors_list

    def create_color_border_list_for_chat(self, colors_list):
        border_color_list = [opacity.replace("0.6", "1") for opacity in colors_list]
        return border_color_list


class DeleteFaceView(TemplateView):
    template_name = "delete.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        queryset = FacebookChatModel.objects.all()
        queryset.delete()
        return context


class FacebookDownloadView(TemplateView):
    template_name = "how_to_download_facebook.html"

class ChattyPrivacyPolicy(TemplateView):
    template_name = "privacy.html"
